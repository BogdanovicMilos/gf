from typing import Tuple

from rest_framework.request import Request
from rest_framework.authentication import SessionAuthentication
from authentication.models import User


class SessionAuthenticationWithRequiredCSRF(SessionAuthentication):
    def authenticate(self, request: Request) -> Tuple[User, None]:
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """

        # Get the session-based user from the underlying HttpRequest object
        user = getattr(request._request, "user", None)

        self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)
