from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from authentication.permissions import IsAuthenticated, IsGrowthFoundryUser


class TeamsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsGrowthFoundryUser]

    def get(self, request: Request) -> Response:
        return Response(template_name="dashboard/teams.html")
