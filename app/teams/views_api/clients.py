import json

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from authentication.permissions import IsAuthenticated
from teams.models import Client
from teams.repositories import ClientRepository
from teams.serializers import ClientSerializer


class ClientsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ClientsApiView(APIView, ClientsPagination):
    permission_classes = [IsAuthenticated]
    filter_fields = (
        "id",
        "company_name",
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

    def get(self, request: Request) -> Response:
        queryset = Client.objects.filter(team=request.user.team)

        params = request.query_params
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
        return self.get_paginated_response(ClientSerializer(page, many=True).data)

    def post(self, request: Request) -> Response:
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client = Client(company_name=serializer.validated_data.get("company_name"), team=request.user.team)

        ClientRepository.save(client)

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data})
