# Generated by Django 3.0.8 on 2021-01-15 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieswipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote_system_model',
            name='username',
        ),
        migrations.AddField(
            model_name='vote_system_model',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
