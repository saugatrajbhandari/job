from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
from django.core.files import File
import pathlib
from django.conf import settings

@shared_task(bind=True)
def send_email(self, email_from, message, fileurl):
    f = str(settings.BASE_DIR) + fileurl
    file = open(f, "rb")
    email = EmailMessage('New application received', message, settings.EMAIL_HOST_USER,
    [settings.EMAIL_TO], headers={'Reply-To': email_from})
    email.attach(file.name, file.read())
    email.send()
