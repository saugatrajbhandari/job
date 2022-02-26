from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage


@shared_task(bind=True)
def send_email(self, email_from, message, file):
    email = EmailMessage('New application received', message, email_from,
    ['nepal@gmail.com', ], headers={'Reply-To': email_from})
    email.attach(file.name, file.read(), file.content_type)
    email.send()
