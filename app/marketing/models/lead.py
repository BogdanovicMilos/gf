from django.db import models
from utils.models import BaseModel


class Lead(BaseModel):
    LESS_THAN_10_THOUSAND = "less_than_10_thousand"
    BETWEEN_10_AND_25_THOUSAND = "between_10_and_25_thousand"
    BETWEEN_25_AND_50_THOUSAND = "between_25_and_50_thousand"
    BETWEEN_50_AND_100_THOUSAND = "between_50_and_100_thousand"
    MORE_THAN_100_THOUSAND = "more_than_100_thousand"

    MONTHLY_AD_BUDGET_CHOICES = [
        (LESS_THAN_10_THOUSAND, "Less than $10,000/month"),
        (BETWEEN_10_AND_25_THOUSAND, "$10,000-$25,000/month"),
        (BETWEEN_25_AND_50_THOUSAND, "$25,001-$50,000/month"),
        (BETWEEN_50_AND_100_THOUSAND, "$50,001-$100,000/month"),
        (MORE_THAN_100_THOUSAND, "$100,000+/month"),
    ]

    full_name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=30)
    email_address = models.EmailField(null=True, blank=True, unique=True)
    website = models.URLField(blank=True)
    monthly_ad_budget = models.CharField(max_length=30, choices=MONTHLY_AD_BUDGET_CHOICES, blank=True)
    message = models.TextField(blank=True)
