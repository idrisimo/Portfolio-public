# Generated by Django 3.0.8 on 2020-11-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker_app', '0006_auto_20201112_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense_category_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
