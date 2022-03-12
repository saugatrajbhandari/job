from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='email address')

    def __str__(self):
        return self.email
