from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated
from teams.permissions import IsClientInsideTenant
from teams.repositories import ClientRepository
from teams.serializers import ClientSerializer


class ClientApiView(APIView):
    permission_classes = [IsAuthenticated, IsClientInsideTenant]

    def get(self, request: Request, client_id: int) -> Response:
        if not (client := ClientRepository.get(client_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, client_id: int) -> Response:
        if not (client := ClientRepository.get(client_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        client = ClientRepository.delete(client_id)

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, client_id: int) -> Response:
        if not (client := ClientRepository.get(client_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        client.company_name = serializer.validated_data.get("company_name", client.company_name)

        ClientRepository.save(client)

        serializer = ClientSerializer(client)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
