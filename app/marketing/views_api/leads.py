import json

from django.db.models import Q

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from authentication.permissions import IsAuthenticated, IsGrowthFoundryUser
from marketing.models import Lead
from marketing.repositories.lead import LeadRepository
from marketing.serializers import LeadSerializer


class LeadsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class LeadsApiView(APIView, LeadsPagination):
    permission_classes = [IsAuthenticated, IsGrowthFoundryUser]
    filter_fields = (
        "id",
        "full_name",
        "phone_number",
        "email_address",
        "website",
        "monthly_ad_budget",
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
        """
        filtering example:
        http://localhost:8000/leads/?full_name=Koray
        filtering with paging example:
        http://localhost:8000/leads/?full_name=Koray&page_size=10
        sorting with paging example:
        http://localhost:8000/leads/?page_size=10&ordering=-id
        """
        params = request.query_params
        if params.get("searchTerm", None):
            search_term = params.get("searchTerm")
            queryset = Lead.objects.filter(
                Q(full_name__icontains=search_term)
                | Q(phone_number__icontains=search_term)
                | Q(email_address__icontains=search_term)
                | Q(website__icontains=search_term)
                | Q(monthly_ad_budget__icontains=search_term)
            ).distinct()
        else:
            queryset = LeadRepository.all()

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
        return self.get_paginated_response(LeadSerializer(page, many=True).data)
