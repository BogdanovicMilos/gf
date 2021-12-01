from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated
from teams.permissions import IsWebPageInsideTenant
from teams.repositories import WebPageRepository
from teams.serializers import WebPageSerializer


class WebPageApiView(APIView):
    permission_classes = [IsAuthenticated, IsWebPageInsideTenant]

    def get(self, request: Request, webpage_id: int) -> Response:
        if not (webpage := WebPageRepository.get(webpage_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebPageSerializer(webpage)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, webpage_id: int) -> Response:
        if not (webpage := WebPageRepository.get(webpage_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        webpage = WebPageRepository.delete(webpage_id)

        serializer = WebPageSerializer(webpage)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, webpage_id: int) -> Response:
        if not (webpage := WebPageRepository.get(webpage_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebPageSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        webpage.url = serializer.validated_data.get("url", webpage.url)

        WebPageRepository.save(webpage)

        serializer = WebPageSerializer(webpage)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
