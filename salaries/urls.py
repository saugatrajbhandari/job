from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalariesListView.as_view(), name='salaries')
]
