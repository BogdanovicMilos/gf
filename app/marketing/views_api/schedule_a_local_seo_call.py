from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from marketing.models import Lead
from marketing.repositories import LeadRepository
from marketing.tasks.send_email import send_lead_notification_email_task
from marketing.serializers import ScheduleLocalSeoCallSerializer, LeadSerializer


class ScheduleAdStrategyCallApiView(APIView):
    @staticmethod
    def post(request: Request) -> Response:
        serializer = ScheduleLocalSeoCallSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        lead = Lead(
            full_name=serializer.validated_data.get("full_name"),
            email_address=serializer.validated_data.get("email_address"),
            phone_number=serializer.validated_data.get("phone_number"),
            website=serializer.validated_data.get("website"),
            monthly_ad_budget=serializer.validated_data.get("monthly_ad_budget"),
        )
        LeadRepository.save(lead)

        send_lead_notification_email_task.delay(
            subject="Schedule Ad Strategy Call",
            full_name=lead.full_name,
            phone_number=lead.phone_number,
            email_address=lead.email_address,
            website=lead.website,
            monthly_ad_budget=lead.monthly_ad_budget,
        )

        serializer = LeadSerializer(lead)
        return Response({"data": serializer.data})
