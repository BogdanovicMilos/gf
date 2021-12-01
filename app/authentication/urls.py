from django.urls import path, include
from .views_api import UsersApiView, UserApiView


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("api/users/", UsersApiView.as_view(), name="users"),
    path("api/users/<int:user_id>/", UserApiView.as_view(), name="user"),
]
