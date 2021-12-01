from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated
from teams.permissions import IsWebsiteInsideTenant
from teams.repositories import WebsiteRepository
from teams.serializers import WebsiteSerializer


class WebsiteApiView(APIView):
    permission_classes = [IsAuthenticated, IsWebsiteInsideTenant]

    def get(self, request: Request, website_id: int) -> Response:
        if not (website := WebsiteRepository.get(website_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebsiteSerializer(website)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, website_id: int) -> Response:
        if not (website := WebsiteRepository.get(website_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        website = WebsiteRepository.delete(website_id)

        serializer = WebsiteSerializer(website)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, website_id: int) -> Response:
        if not (website := WebsiteRepository.get(website_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WebsiteSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        website.name = data.get("name", website.name)
        website.domain = data.get("domain", website.domain)

        WebsiteRepository.save(website)

        serializer = WebsiteSerializer(website)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
