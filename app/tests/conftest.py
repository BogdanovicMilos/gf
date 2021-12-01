from pytest_factoryboy import register

from django.test import Client

from .factories.lead_factory import LeadFactory
from .factories.user_factory import UserFactory
from .factories.website_factory import WebsiteFactory
from .factories.webpage_factory import WebpageFactory
from .factories.team_factory import TeamFactory
from .factories.client_factory import ClientFactory


register(LeadFactory)
register(UserFactory)
register(WebsiteFactory)
register(WebpageFactory)
register(TeamFactory)
register(ClientFactory)

client = Client
