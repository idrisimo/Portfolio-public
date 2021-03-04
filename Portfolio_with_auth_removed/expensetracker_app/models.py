from django.db import models



class Expenses_model(models.Model):
    is_expense = models.CharField(max_length=7)
    date = models.DateField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

class Expense_category_model(models.Model):
    category_item = models.CharField(max_length=20)

    def __str__(self):
        return self.category_item
