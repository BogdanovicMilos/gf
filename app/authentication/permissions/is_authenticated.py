from typing import cast

from django.views import View

from rest_framework.request import Request
from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return cast(bool, request.user and request.user.is_authenticated)
