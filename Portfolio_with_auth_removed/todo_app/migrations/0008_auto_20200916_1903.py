# Generated by Django 3.0.8 on 2020-09-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_remove_todo_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='list_item',
            field=models.CharField(default='tert', max_length=100),
            preserve_default=False,
        ),
    ]
