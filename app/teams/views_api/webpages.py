import json

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from authentication.permissions import IsAuthenticated
from teams.permissions import IsWebsiteInsideTenant
from teams.models import WebPage
from teams.repositories import WebsiteRepository, WebPageRepository
from teams.serializers import WebPageSerializer


class WebPagesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class WebPagesApiView(APIView, WebPagesPagination):
    permission_classes = [IsAuthenticated, IsWebsiteInsideTenant]
    filter_fields = (
        "id",
        "url",
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

    def get(self, request: Request, website_id: int) -> Response:
        if not (website := WebsiteRepository.get(website_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = WebPage.objects.filter(website__client__team=request.user.team, website=website)

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
        return self.get_paginated_response(WebPageSerializer(page, many=True).data)

    def post(self, request: Request, website_id: int) -> Response:
        if not (website := WebsiteRepository.get(website_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebPageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        webpage = WebPage(
            url=serializer.validated_data.get("url"),
            website=website,
        )

        WebPageRepository.save(webpage)

        serializer = WebPageSerializer(webpage)
        return Response({"data": serializer.data})
