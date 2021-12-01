import factory

from teams.models.website import Website


class WebsiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Website

    name = factory.Faker("name")
    domain = factory.Faker("url")
