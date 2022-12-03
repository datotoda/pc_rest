from django.conf import settings
from django.core import mail

from celery import shared_task


@shared_task
def send_mail(subject=None, body=None, to=None):
    return mail.send_mail(
        subject=subject,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=to
    )
