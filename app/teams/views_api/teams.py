import json

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated, IsGrowthFoundryUser
from teams.models import Team
from teams.repositories import TeamRepository
from teams.serializers import TeamSerializer


class TeamsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class TeamsApiView(APIView, TeamsPagination):
    permission_classes = [IsAuthenticated, IsGrowthFoundryUser]
    filter_fields = ("id", "name")

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
        queryset = TeamRepository.all()

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
        return self.get_paginated_response(TeamSerializer(page, many=True).data)

    def post(self, request: Request) -> Response:
        serializer = TeamSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        team = Team(
            name=serializer.validated_data.get("name"),
        )

        TeamRepository.save(team)

        serializer = TeamSerializer(team)
        return Response({"data": serializer.data})
