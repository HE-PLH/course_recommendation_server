# Generated by Django 3.2.9 on 2023-08-06 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_subjectweight_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectweight',
            name='response',
        ),
    ]
