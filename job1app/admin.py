from django.contrib import admin
from .models import Category, Job


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'type', 'salary']
    readonly_fields = ('created', 'updated')