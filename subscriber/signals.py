from .models import Subscriber
from job1app.models import Job
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from .tasks import send_email


def create_subscriber(sender, instance, created, **kwargs):
    print('before created')
    print(dir(instance))
    if created:
        print('created')
        current_site = Site.objects.get_current()
        slug = instance.slug
        message = render_to_string('subscriber/job_alert_email.html', {'slug': slug, 'current_site':current_site})
        send_email.delay(message)


post_save.connect(create_subscriber, sender=Job)
