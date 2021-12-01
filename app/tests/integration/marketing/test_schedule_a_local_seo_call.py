import pytest

from marketing.models import Lead


@pytest.mark.integration
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_schedule_a_local_seo_call(client):
    data = {
        "full_name": "Name Surname",
        "phone_number": "+374123456789",
        "email_address": "name@example.com",
        "website": "website.com",
        "monthly_ad_budget": Lead.MONTHLY_AD_BUDGET_CHOICES[0][0],
        "message": "",
    }

    response = client.post("/api/schedule-a-local-seo-call/", data, content_type="application/json")

    assert response.status_code == 200
    assert response.json() == {"data": {"id": 1, **data}}

    lead = Lead.objects.get(id=1)
    assert lead is not None
    assert lead.email_address == data["email_address"]


@pytest.mark.integration
def test_schedule_a_local_seo_call_invalid_data(client):
    invalid_data = {"full_name": "Name Surname", "email_address": ""}

    response = client.post("/api/schedule-a-local-seo-call/", invalid_data, content_type="application/json")

    assert response.status_code == 400
    assert response.json() == {
        "phone_number": ["This field is required."],
        "email_address": ["This field may not be blank."],
        "website": ["This field is required."],
        "monthly_ad_budget": ["This field is required."],
    }
