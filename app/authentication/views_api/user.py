from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from authentication.repositories.user import UserRepository
from authentication.serializers.user import UserSerializer
from authentication.permissions import IsAuthenticated, IsUserInsideTenant


User = get_user_model()


class UserApiView(APIView):
    permission_classes = [IsAuthenticated, IsUserInsideTenant]

    def get(self, request: Request, user_id: int) -> Response:
        if not (user := UserRepository.get(user_id)):
            return Response(status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, user_id: int) -> Response:
        if not (user := UserRepository.delete(user_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, user_id: int) -> Response:
        if request.user.id != user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if not (user := UserRepository.get(user_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        user.email = serializer.validated_data.get("email", user.email)

        UserRepository.save(user)

        serializer = UserSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
