# Generated by Django 3.0.8 on 2020-10-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urlmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=100)),
                ('short_string', models.CharField(max_length=50)),
            ],
        ),
    ]
