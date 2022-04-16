from django.db import models
from django.conf import settings
from users.models import User


class CompanyAccount(models.Model):
    username = models.CharField(verbose_name='Your Name', max_length=255)
    company_name = models.CharField(verbose_name='Company Name', max_length=255)
    email = models.EmailField(verbose_name='Email', max_length=255)
    password = models.CharField(verbose_name='Password', max_length=50)

    def __str__(self):
        return self.company_name


