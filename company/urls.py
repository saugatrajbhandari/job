from django.urls import path

from .views import JobPostView

urlpatterns = [
    path('post_job/', JobPostView.as_view(), name='post_job'),
]