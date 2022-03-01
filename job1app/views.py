from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from .models import Category, Job
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files import File
from .tasks import send_email
import json
from pathlib import Path
from django.core.files.storage import FileSystemStorage



def home(request):
    job = Job.active.all()
    return render(request, 'job1app/home.html', {'job': job})


def job_category(request):
    jobs = Job.objects.filter(category__name='job', is_active=True)
    return render(request, 'job1app/job_category.html', {'jobs': jobs})


def internship_category(request):
    internships = Job.objects.filter(category__name='internship', is_active=True)
    return render(request, 'job1app/internship_category.html', {'internships': internships})


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

        # email = EmailMessage('New application received', message, email_from,
        #                      [settings.EMAIL_TO], headers={'Reply-To': email_from})
        fs = FileSystemStorage()
        f = fs.save(file.name, file)
        fileurl = fs.url(f)
        print(fileurl)
        filename = file.name
        extension = filename.split('.')
        if extension[1] != 'txt' and extension[1] != 'pdf' and extension[1] != 'text':
            print(type(extension[1]))
            messages.add_message(request, messages.ERROR, "Not an appropriate file format!")
            return redirect('job-detail', slug=slug)
        send_email.delay(email_from, message, fileurl)
        messages.add_message(request, messages.SUCCESS, "Application send successfully!")
        return redirect('job-detail', slug=slug)

    return render(request, 'job1app/job_detail.html')
