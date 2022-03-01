from django.urls import path
from .views import home, job_detail, apply, job_category, internship_category


urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>', job_detail, name="job-detail"),
    path('apply/', apply, name='apply'),
    path('jobs/', job_category, name='job-category'),
    path('internships/', internship_category, name='internship-category'),
]
