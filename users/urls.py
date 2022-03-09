from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (user_register, account_activate, LogoutView)
from .forms import UserLoginForm

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html',
                                        form_class=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<slug:uidb64>/<slug:token>)/', account_activate, name='activate'),
]