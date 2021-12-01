from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated, IsGrowthFoundryUser
from marketing.repositories.lead import LeadRepository
from marketing.serializers import LeadSerializer


class LeadApiView(APIView):
    permission_classes = [IsAuthenticated, IsGrowthFoundryUser]

    def get(self, request: Request, lead_id: int) -> Response:
        if not (lead := LeadRepository.get(lead_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(lead)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, lead_id: int) -> Response:
        if not (lead := LeadRepository.delete(lead_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(lead)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, lead_id: int) -> Response:
        if not (lead := LeadRepository.get(lead_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        lead.full_name = data.get("full_name", lead.full_name)
        lead.phone_number = data.get("phone_number", lead.phone_number)
        lead.email_address = data.get("email_address", lead.email_address)
        lead.website = data.get("website", lead.website)
        lead.monthly_ad_budget = data.get("monthly_ad_budget", lead.monthly_ad_budget)
        lead.message = data.get("message", lead.message)

        LeadRepository.save(lead)

        serializer = LeadSerializer(lead)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
