from typing import cast, Optional
from django.db.models.query import QuerySet

from teams.models import Team


class TeamRepository:
    @staticmethod
    def all() -> QuerySet:
        return Team.objects.all()

    @staticmethod
    def save(team: Team) -> Team:
        team.save()
        return team

    @staticmethod
    def get(team_id: int) -> Optional[Team]:
        try:
            team = Team.objects.get(id=team_id)
            return cast(Team, team)
        except Team.DoesNotExist:
            return None

    @staticmethod
    def delete(team_id: int):
        if team := TeamRepository.get(team_id):
            team.delete()

        return cast(Team, team)

    @staticmethod
    def is_dirty(team: Team) -> bool:
        return cast(bool, team.is_dirty())
