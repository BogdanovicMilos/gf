from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from authentication.permissions import IsAuthenticated


class ClientsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(template_name="dashboard/clients.html")
