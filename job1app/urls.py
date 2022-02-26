from django.urls import path
from .views import home, job_detail, apply


urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>', job_detail, name="job-detail"),
    path('apply/', apply, name='apply'),
]
