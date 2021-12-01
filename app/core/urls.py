from django.urls import path, include
from .views import dashboard
import debug_toolbar


urlpatterns = [
    path("", include("authentication.urls")),
    path("", include("marketing.urls")),
    path("", include("teams.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("__debug__/", include(debug_toolbar.urls)),
]
