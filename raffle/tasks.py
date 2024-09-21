from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_task(subject, message, recipient_email):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [recipient_email])
