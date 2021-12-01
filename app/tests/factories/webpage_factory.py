import factory

from teams.models.webpage import WebPage
from .website_factory import WebsiteFactory


class WebpageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WebPage

    url = factory.Faker("url")
    website = factory.SubFactory(WebsiteFactory)
