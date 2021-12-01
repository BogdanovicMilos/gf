import pytest

from marketing.models import Lead


@pytest.mark.integration
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_schedule_a_call(client):
    data = {"full_name": "Name Surname", "phone_number": "+374123456789"}

    response = client.post("/api/schedule-a-call/", data, content_type="application/json")

    assert response.status_code == 200
    assert response.json() == {
        "data": {"id": 1, "monthly_ad_budget": "", "email_address": None, "website": "", "message": "", **data}
    }

    lead = Lead.objects.get(id=1)
    assert lead is not None
    assert lead.full_name == data["full_name"]


@pytest.mark.integration
def test_schedule_a_call_invalid_data(client):
    data = {"full_name": "", "phone_number": "+374123456789"}

    response = client.post("/api/schedule-a-call/", data, content_type="application/json")

    assert response.status_code == 400
    assert response.json() == {"full_name": ["This field may not be blank."]}
