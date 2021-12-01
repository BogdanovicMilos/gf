import json

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from authentication.serializers.user import UserSerializer
from authentication.permissions import IsAuthenticated


User = get_user_model()


class UsersApiView(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated]
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
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
        queryset = User.objects.filter(team=request.user.team)

        params = request.query_params
        if params.get("searchTerm", None):
            search_term = params.get("searchTerm")
            queryset = queryset.filter(email__icontains=search_term).distinct()

        if params.get("email", None):
            queryset = queryset.filter(email=params.get("email"))

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
        return self.get_paginated_response(UserSerializer(page, many=True).data)
