# Generated by Django 4.0.2 on 2022-02-22 14:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job1app', '0004_job_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
