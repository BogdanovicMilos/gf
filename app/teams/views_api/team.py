from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsAuthenticated, IsGrowthFoundryUser
from teams.permissions import IsTeamInsideTenant
from teams.repositories import TeamRepository
from teams.serializers import TeamSerializer


class TeamApiView(APIView):
    permission_classes = [IsAuthenticated, IsGrowthFoundryUser, IsTeamInsideTenant]

    def get(self, request: Request, team_id: int) -> Response:
        if not (team := TeamRepository.get(team_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        if not (team := TeamRepository.delete(team_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team)
        return Response({"data": serializer.data}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, team_id: int) -> Response:
        if not (team := TeamRepository.get(team_id)):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        team.name = serializer.validated_data.get("name", team.name)

        TeamRepository.save(team)

        serializer = TeamSerializer(team)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
