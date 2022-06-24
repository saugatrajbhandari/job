from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages

from .forms import CompanyAccountRegistrationForm, CompanyAccountLoginForm
from job1app.models import Job
from job1app.forms import JobForm


class JobPostView(LoginRequiredMixin, CreateView):

    template_name = 'company/post_job.html'
    form_class = JobForm
    success_url = reverse_lazy('create_company_account')
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            messages.warning(request, 'You must be a superuser to post a job')
            return redirect('/')
        return super(JobPostView, self).dispatch(request, *args, **kwargs)
