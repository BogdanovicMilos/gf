import pytest


@pytest.mark.integration
@pytest.mark.django_db
def test_leads_pagination(client, user_factory, lead_factory):
    leads = lead_factory.create_batch(30)

    user = user_factory.create()
    client.force_login(user)

    response = client.get("/leads/", {"page": "2"})

    assert response.status_code == 200
    assert response.data["metadata"] == {
        "count": len(leads),
        "previous": "http://testserver/leads/",
        "next": "http://testserver/leads/?page=3",
    }


@pytest.mark.integration
@pytest.mark.django_db
def test_leads_filtering(client, user_factory, lead_factory):
    user = user_factory.create()
    client.force_login(user)

    response = client.get("/leads/", {"full_name": "Name Surname"})

    assert response.status_code == 200
    assert response.data == {"data": [], "metadata": {}}

    lead = lead_factory.create()

    response = client.get("/leads/", {"full_name": lead.full_name})

    assert response.status_code == 200
    assert response.data == {
        "data": [
            {
                "id": lead.id,
                "full_name": lead.full_name,
                "phone_number": lead.phone_number,
                "email_address": lead.email_address,
                "website": lead.website,
                "monthly_ad_budget": lead.monthly_ad_budget,
                "message": lead.message,
            }
        ],
        "metadata": {"count": 1, "previous": None, "next": None},
    }


@pytest.mark.integration
@pytest.mark.django_db
def test_leads_ordering(client, user_factory, lead_factory):
    user = user_factory.create()
    client.force_login(user)

    lead_1 = lead_factory.create()
    lead_2 = lead_factory.create()

    # response = client.get('/leads/', {'ordering': '-id'})
    response = client.get("/leads/", {"sort[]": '{"type":"desc", "field":"id"}'})

    assert response.status_code == 200
    assert response.data == {
        "data": [
            {
                "id": lead_2.id,
                "full_name": lead_2.full_name,
                "phone_number": lead_2.phone_number,
                "email_address": lead_2.email_address,
                "website": lead_2.website,
                "monthly_ad_budget": lead_2.monthly_ad_budget,
                "message": lead_2.message,
            },
            {
                "id": lead_1.id,
                "full_name": lead_1.full_name,
                "phone_number": lead_1.phone_number,
                "email_address": lead_1.email_address,
                "website": lead_1.website,
                "monthly_ad_budget": lead_1.monthly_ad_budget,
                "message": lead_1.message,
            },
        ],
        "metadata": {"count": 2, "previous": None, "next": None},
    }
