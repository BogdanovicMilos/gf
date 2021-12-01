import pytest

from marketing.models import Lead


@pytest.mark.integration
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_send_us_a_message(client):
    data = {"full_name": "Name Surname", "phone_number": "+374123456789", "message": "Hello"}

    response = client.post("/api/send-us-a-message/", data, content_type="application/json")

    assert response.status_code == 200
    assert response.json() == {
        "data": {"id": 1, "monthly_ad_budget": "", "email_address": None, "website": "", **data}
    }

    lead = Lead.objects.get(id=1)
    assert lead is not None
    assert lead.full_name == data["full_name"]


@pytest.mark.integration
def test_send_us_a_message_invalid_data(client):
    invalid_data = {"full_name": "Name Surname", "phone_number": ""}

    response = client.post("/api/send-us-a-message/", invalid_data, content_type="application/json")

    assert response.status_code == 400
    assert response.json() == {
        "phone_number": ["This field may not be blank."],
        "message": ["This field is required."],
    }
