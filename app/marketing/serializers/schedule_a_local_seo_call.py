from rest_framework.serializers import Serializer, CharField, EmailField, ChoiceField
from marketing.models import Lead


class ScheduleLocalSeoCallSerializer(Serializer):
    full_name = CharField(max_length=254)
    phone_number = CharField(max_length=30)
    email_address = EmailField()
    website = CharField()
    monthly_ad_budget = ChoiceField(choices=Lead.MONTHLY_AD_BUDGET_CHOICES)
