import structlog
from typing import List
from django.core.mail import send_mail

logger = structlog.getLogger(__name__)


def send_multipart_alternative_email(recipients: List[str], subject: str, content_html: str, content_txt: str) -> None:
    try:
        send_mail(
            subject=subject,
            message=content_txt,
            from_email="noreply@growthfoundry.com",
            recipient_list=recipients,
            html_message=content_html,
        )
    except Exception as exc:
        logger.exception("error", exc_info=exc)
