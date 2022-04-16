from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CompanyAccount

admin.site.register(CompanyAccount)