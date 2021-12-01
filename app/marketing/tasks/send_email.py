from django.conf import settings
from django.template.loader import render_to_string

from core.celery import app
from utils.email import send_multipart_alternative_email


@app.task
def send_lead_notification_email_task(**kwargs) -> None:
    msg_txt = render_to_string("marketing/email/new_lead_notification_email.txt", kwargs)
    msg_html = render_to_string("marketing/email/new_lead_notification_email.html", kwargs)
    recipients = settings.NEW_LEAD_NOTIFICATION_RECIPIENTS
    subject = f"New Growth Foundry lead {kwargs['full_name']} [{kwargs['subject']}]"
    send_multipart_alternative_email(recipients, subject, msg_html, msg_txt)
