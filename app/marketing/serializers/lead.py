from rest_framework.serializers import Serializer, IntegerField, CharField, EmailField, ChoiceField
from marketing.models import Lead


class LeadSerializer(Serializer):
    id = IntegerField(read_only=True)
    full_name = CharField(max_length=254)
    phone_number = CharField(max_length=30)
    email_address = EmailField(required=False, allow_null=True, allow_blank=True)
    website = CharField(required=False, allow_null=True, allow_blank=True)
    monthly_ad_budget = ChoiceField(
        choices=Lead.MONTHLY_AD_BUDGET_CHOICES, required=False, allow_null=True, allow_blank=True
    )
    message = CharField(required=False, allow_null=True, allow_blank=True)
