from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import (TemplateView, ListView, DetailView)
from django.core.paginator import Paginator

from taggit.models import Tag
from rest_framework.generics import ListAPIView

from .models import Category, Job
from .tasks import send_email
from .serializers import JobSerializer


class HomeView(ListView):
    template_name = 'job1app/home.html'
    context_object_name = 'jobs'
    model = Job

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class JobList(ListAPIView):
    queryset = Job.active.all()
    serializer_class = JobSerializer


class JobCategoryView(ListView):
    template_name = 'job1app/job_category.html'
    context_object_name = 'jobs'
    paginate_by = 5

    def get_queryset(self):
        return Job.objects.filter(category__name='job', is_active=True)


class InternshipCategoryView(ListView):
    template_name = 'job1app/internship_category.html'
    context_object_name = 'internships'
    paginate_by = 5

    def get_queryset(self):
        return Job.objects.filter(category__name='internship', is_active=True)


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'job1app/job_detail.html'


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


def search(request):
    home_search_text = request.GET.get('q')
    print(home_search_text)
    if home_search_text:
        qs = Job.objects.filter(title__icontains=home_search_text)

    job_category_text = request.GET.get('r')
    if job_category_text:
        job_category = Category.objects.get(name='job')
        qs = job_category.category.filter(title__icontains=job_category_text)

    internship_category_text = request.GET.get('s')
    if internship_category_text:
        internship_category = Category.objects.get(name='internship')
        qs = internship_category.category.filter(title__icontains=internship_category_text)

    return render(request, 'job1app/search.html', {'qs': qs})
