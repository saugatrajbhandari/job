from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import Subscriber


@shared_task(bind=True)
def send_email(self, message):
    send_mail('new job added', message, settings.EMAIL_HOST_USER,
              [subscriber.email for subscriber in Subscriber.objects.all()],
              fail_silently=False)
