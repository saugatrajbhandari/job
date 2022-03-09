from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class JobActiveManager(models.Manager):
    def get_queryset(self):
        return super(JobActiveManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    """
    here we define what type of work is it
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    job_type = (
        ('non remote', 'non remote'),
        ('remote', 'remote')
    )
    title = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, null=True)
    apply_before = models.DateField(verbose_name='apply before', null=True, blank=True)
    education_level = models.CharField(verbose_name='education level', max_length=255, blank=True, null=True)
    no_of_vacancy = models.CharField(verbose_name='number of vacancy', max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    specification = RichTextField(verbose_name='job specification', blank=True)
    requirement = RichTextField(verbose_name='technical requirement', blank=True, null=True)
    benefit = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    organization = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    work_day = models.IntegerField(default=6)
    type = models.CharField(max_length=20, choices=job_type, default='non remote')
    # for internship
    is_paid = models.BooleanField(default=True, help_text="for internship only")
    duration = models.CharField(max_length=255, blank=True, null=True, help_text="for internship only")
    additional_benefits = models.BooleanField(blank=True, null=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    active = JobActiveManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title+" " + self.organization)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})



