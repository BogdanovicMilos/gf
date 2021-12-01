from django.urls import path

from .views import TeamsView, ClientsView, WebsitesView, WebPagesView
from .views_api import (
    TeamsApiView,
    TeamApiView,
    ClientsApiView,
    ClientApiView,
    WebsitesApiView,
    WebsiteApiView,
    WebPagesApiView,
    WebPageApiView,
)


urlpatterns = [
    path("dashboard/teams/", TeamsView.as_view(), name="dashboard_teams"),
    path("api/teams/", TeamsApiView.as_view(), name="teams"),
    path("api/teams/<int:team_id>/", TeamApiView.as_view(), name="team"),
    path("dashboard/clients/", ClientsView.as_view(), name="dashboard_clients"),
    path("api/clients/", ClientsApiView.as_view(), name="clients"),
    path("api/clients/<int:client_id>/", ClientApiView.as_view(), name="client"),
    path("dashboard/clients/<int:client_id>/websites/", WebsitesView.as_view(), name="dashboard_websites"),
    path("api/clients/<int:client_id>/websites/", WebsitesApiView.as_view(), name="websites"),
    path("api/websites/<int:website_id>/", WebsiteApiView.as_view(), name="website"),
    path(
        "dashboard/websites/<int:website_id>/webpages/",
        WebPagesView.as_view(),
        name="dashboard_webpages",
    ),
    path("api/websites/<int:website_id>/webpages/", WebPagesApiView.as_view(), name="webpages"),
    path(
        "api/webpages/<int:webpage_id>/",
        WebPageApiView.as_view(),
        name="webpage",
    ),
]
