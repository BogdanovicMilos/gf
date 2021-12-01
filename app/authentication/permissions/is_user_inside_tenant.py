from typing import cast

from django.views import View
from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.permissions import BasePermission

from authentication.models import User


class IsUserInsideTenant(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user = get_object_or_404(User, pk=view.kwargs["user_id"])
        return cast(bool, request.user.team.id == user.team.id)
