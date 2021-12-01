import pytest

from marketing.models import Lead


@pytest.mark.integration
@pytest.mark.django_db
def test_update_lead(client, user_factory, lead_factory):
    lead = lead_factory.create()

    user = user_factory.create()
    client.force_login(user)

    response = client.put(f"/leads/{lead.id}", {"full_name": "Name Surname"}, content_type="application/json")

    lead = Lead.objects.get(id=lead.id)

    assert response.status_code == 200
    assert response.data == {
        "data": {
            "id": lead.id,
            "full_name": lead.full_name,
            "phone_number": lead.phone_number,
            "email_address": lead.email_address,
            "website": lead.website,
            "monthly_ad_budget": lead.monthly_ad_budget,
            "message": lead.message,
        }
    }


@pytest.mark.integration
@pytest.mark.django_db
def test_update_lead_invalid_id(client, user_factory):
    user = user_factory.create()
    client.force_login(user)

    response = client.put("/leads/100", {}, content_type="application/json")

    assert response.status_code == 404


@pytest.mark.integration
@pytest.mark.django_db
def test_update_lead_forbidden(client, user_factory, lead_factory):
    lead = lead_factory.create()

    response = client.put(f"/leads/{lead.id}", {}, content_type="application/json")
    assert response.status_code == 403

    user = user_factory.build(email="name@example.com")
    user.save()

    client.force_login(user)

    response = client.put(f"/leads/{lead.id}", {}, content_type="application/json")
    assert response.status_code == 403
