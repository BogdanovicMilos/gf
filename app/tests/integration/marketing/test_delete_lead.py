import pytest


@pytest.mark.integration
@pytest.mark.django_db
def test_delete_lead(client, user_factory, lead_factory):
    lead = lead_factory.create()

    user = user_factory.create()
    client.force_login(user)

    response = client.delete(f"/leads/{lead.id}")

    assert response.status_code == 204
    assert response.data == {
        "data": {
            "id": None,
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
def test_delete_lead_invalid_id(client, user_factory):
    user = user_factory.create()
    client.force_login(user)

    response = client.delete("/leads/100")

    assert response.status_code == 404


@pytest.mark.integration
@pytest.mark.django_db
def test_update_lead_forbidden(client, user_factory, lead_factory):
    lead = lead_factory.create()

    response = client.delete(f"/leads/{lead.id}")
    assert response.status_code == 403

    user = user_factory.build(email="name@example.com")
    user.save()

    client.force_login(user)

    response = client.delete(f"/leads/{lead.id}")
    assert response.status_code == 403
