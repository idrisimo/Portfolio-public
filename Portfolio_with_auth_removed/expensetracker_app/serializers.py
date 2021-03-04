from rest_framework import serializers
from .models import Expenses_model, Expense_category_model

class Expense_serializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses_model
        fields = '__all__'

class Expense_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Expense_category_model
        fields = '__all__'
