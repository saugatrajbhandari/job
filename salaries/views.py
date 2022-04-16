from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Salary
from .forms import SalaryModelForm


class SalariesListView(CreateView):
    model = Salary
    template_name = 'salaries/salaries.html'
    form_class = SalaryModelForm
    success_url = reverse_lazy('salaries')

    def get_context_data(self, **kwargs):
        context = super(SalariesListView, self).get_context_data(**kwargs)
        context['salaries'] = Salary.objects.all()
        page = self.request.GET.get('page')
        paginator = Paginator(context['salaries'], 6)
        context['page_obj'] = paginator.get_page(page)
        return context

    def form_valid(self, form):
        form = super(SalariesListView, self).form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, "Your job posted successfully!")
        return form

