import factory

from .team_factory import TeamFactory
from teams.models.client import Client


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    company_name = factory.Faker("name")
    team = factory.SubFactory(TeamFactory)
