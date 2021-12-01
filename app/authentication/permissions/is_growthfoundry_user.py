from django.views import View

from rest_framework.request import Request
from rest_framework.permissions import BasePermission


class IsGrowthFoundryUser(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return bool(request.user.is_growthfoundry_user)
