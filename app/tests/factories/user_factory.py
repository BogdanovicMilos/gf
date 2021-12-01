import factory

from .team_factory import TeamFactory
from authentication.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = "gor@growthfoundry.com"
    password = factory.Faker("password")
    team = factory.SubFactory(TeamFactory)
