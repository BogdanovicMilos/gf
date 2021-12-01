import factory

from marketing.models import Lead


class LeadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lead

    full_name = factory.Faker("name")
    phone_number = factory.Faker("phone_number")
    email_address = factory.Faker("email")
    website = factory.Faker("url")
    monthly_ad_budget = factory.Faker(
        "random_element", elements=[items[0] for items in Lead.MONTHLY_AD_BUDGET_CHOICES]
    )
    message = factory.Faker("text")
