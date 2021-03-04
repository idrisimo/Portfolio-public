from django.contrib import admin

from .models import *

admin.site.register(Expenses_model)
admin.site.register(Expense_category_model)