from typing import Union, cast

from django.views import View

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from teams.repositories import WebsiteRepository


class IsWebsiteInsideTenant(BasePermission):
    def has_permission(self, request: Request, view: View) -> Union[Response, bool]:
        if not (website := WebsiteRepository.get(view.kwargs["website_id"])):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return cast(bool, request.user.team.id == website.client.team.id)
