# Generated by Django 3.2.9 on 2023-07-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
            ],
        ),
    ]
