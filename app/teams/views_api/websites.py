import json

from django.db.models import Q

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated
from teams.permissions import IsClientInsideTenant
from teams.models import Website
from teams.repositories import ClientRepository, WebsiteRepository
from teams.serializers import WebsiteSerializer


class WebsitesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class WebsitesApiView(APIView, WebsitesPagination):
    permission_classes = [IsAuthenticated, IsClientInsideTenant]
    filter_fields = (
        "id",
        "name",
        "domain",
    )

    def get_paginated_response(self, data: dict) -> Response:
        return Response(
            {
                "data": data,
                "metadata": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                    "count": self.page.paginator.count,
                },
            },
            status=status.HTTP_200_OK,
        )

    def get(self, request: Request, client_id: int) -> Response:
        if not (client := ClientRepository.get(client_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = Website.objects.filter(client__team=request.user.team, client=client)

        params = request.query_params
        if params.get("searchTerm", None):
            search_term = params.get("searchTerm")
            queryset = queryset.filter(Q(name__icontains=search_term) | Q(domain__icontains=search_term)).distinct()

        if params.get("sort[]", None):
            resp = json.loads(params["sort[]"])
            ordering = "-" if resp["type"] == "desc" else ""
            ordering += resp["field"]
            queryset = queryset.order_by(ordering)

        if params.get("perPage", None):
            page_size = int(params.get("perPage", None))
            self.page_size = page_size if page_size > 0 else queryset.count()

        if not queryset.exists():
            return Response({"data": [], "metadata": {}}, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset, request, view=self)
        return self.get_paginated_response(WebsiteSerializer(page, many=True).data)

    def post(self, request: Request, client_id: int) -> Response:
        if not (client := ClientRepository.get(client_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebsiteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        website = Website(
            name=serializer.validated_data.get("name"),
            domain=serializer.validated_data.get("domain"),
            client=client,
        )

        WebsiteRepository.save(website)

        serializer = WebsiteSerializer(website)
        return Response({"data": serializer.data})
