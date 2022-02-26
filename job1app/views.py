from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from .models import Category, Job
from django.http import HttpResponse
from django.contrib import messages
from .tasks import send_email
from django.core.mail import EmailMessage
from django.conf import settings


def home(request):
    job = Job.objects.all()
    return render(request, 'job1app/home.html', {'job': job})


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'job1app/job_detail.html', {'job': job})


def apply(request):
    if request.method == "POST" and request.FILES['file']:
        slug = request.POST.get('apply')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        file = request.FILES['file']

        context = {'first_name': first_name, 'last_name': last_name, 'email': email, 'slug': slug}
        message = render_to_string('mail_apply.html', context)
        email_from = settings.EMAIL_HOST_USER

        email = EmailMessage('New application received', message, email_from,
                             [settings.EMAIL_TO], headers={'Reply-To': email_from})
        email.attach(file.name, file.read(), file.content_type)
        # await asyncio.create_task(email.send())
        email.send()

        # send_email.delay(email_from, message, file)
        # file = open(file, "r")
        # email.attach_file(file)
        messages.add_message(request, messages.SUCCESS, "Application send successfully!")
        return redirect('job-detail', slug=slug)

    return render(request, 'job1app/job_detail.html')
