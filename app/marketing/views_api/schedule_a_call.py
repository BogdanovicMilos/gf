from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from marketing.models import Lead
from marketing.repositories import LeadRepository
from marketing.serializers import ScheduleCallSerializer, LeadSerializer
from marketing.tasks.send_email import send_lead_notification_email_task


class ScheduleCallApiView(APIView):
    @staticmethod
    def post(request: Request) -> Response:
        serializer = ScheduleCallSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        lead = Lead(
            full_name=serializer.validated_data.get("full_name"),
            phone_number=serializer.validated_data.get("phone_number"),
        )
        LeadRepository.save(lead)
        send_lead_notification_email_task.delay(
            subject="Schedule a call", full_name=lead.full_name, phone_number=lead.phone_number
        )

        serializer = LeadSerializer(lead)
        return Response({"data": serializer.data})
