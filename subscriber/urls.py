from . import views
from django.urls import path

urlpatterns = [
    path('', views.subscriber_view, name='subscriber')
]