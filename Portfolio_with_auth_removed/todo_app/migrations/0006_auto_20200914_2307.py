# Generated by Django 3.0.8 on 2020-09-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_auto_20200914_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='list_item',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
