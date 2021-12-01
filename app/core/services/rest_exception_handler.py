import structlog
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.exceptions import APIException


logger = structlog.getLogger(__name__)


def rest_exception_handler(exc, _):
    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
        logger.exception("Unauthorized", exc_info=exc)
        return Response(
            {"error": "Unauthorized"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    # Handle django rest framework exceptions
    if isinstance(exc, APIException):
        logger.exception("API error", exc_info=exc)
        return Response({"error": exc.detail}, status=exc.status_code)

    logger.exception("error", exc_info=exc)
    return Response(
        {"error": "Sorry, we encountered an internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
