# Generated by Django 3.0.8 on 2020-11-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker_app', '0003_auto_20201112_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses_model',
            name='is_expense',
            field=models.BooleanField(default=True),
        ),
    ]
