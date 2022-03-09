from django.urls import path
from .views import (HomeView, JobCategoryView,
                    apply, InternshipCategoryView, search,
                    JobList, JobDetailView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug:slug>', JobDetailView.as_view(), name="job-detail"),
    path('apply/', apply, name='apply'),
    path('jobs/', JobCategoryView.as_view(), name='job-category'),
    path('internships/', InternshipCategoryView.as_view(), name='internship-category'),
    path('search/', search, name='search'),
    path('job-list/', JobList.as_view(), name='job-list'),
]
