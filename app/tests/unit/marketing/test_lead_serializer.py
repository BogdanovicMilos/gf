from marketing.models import Lead
from marketing.serializers.lead import LeadSerializer


def test_lead_serializer():
    data = {
        "full_name": "Name Surname",
        "phone_number": "+374123456789",
        "email_address": "name@email.com",
        "website": "website.com",
        "monthly_ad_budget": Lead.MONTHLY_AD_BUDGET_CHOICES[0][0],
        "message": "Hello",
    }
    serializer = LeadSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data == data
    assert serializer.data == data
    assert serializer.errors == {}


def test_serializer_invalid_data():
    invalid_data = {"email_address": "email", "monthly_ad_budget": "budget"}
    serializer = LeadSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_data
    assert serializer.errors == {
        "full_name": ["This field is required."],
        "phone_number": ["This field is required."],
        "email_address": ["Enter a valid email address."],
        "monthly_ad_budget": ['"budget" is not a valid choice.'],
    }
