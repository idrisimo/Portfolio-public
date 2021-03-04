from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import Expense_serializer, Expense_category_serializer
from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/expense-list/',
        'Detail View': '/expense-detail/<str:pk>/',
        'Create': '/expense-create/',
        'Update': '/expense-update/<str:pk>/',
        'Delete': '/expense-delete/<str:pk>/',
    }
    return Response(api_urls)

def expensedashboard_view(request):
    example_cat_list = ["Salary",
                        "Groceries",
                        "Entertainment",
                        "Savings",
                        "Bills",
                        "Rent"]
    is_expense_list = ["Expense", "Income"]
    context = {'example_cat_list': example_cat_list, 'is_expense_list': is_expense_list }
    return render(request, 'expense_tracker.html', context)

@api_view(['GET'])
def expense_list(request):
    expenses = Expenses_model.objects.all().order_by('date')
    serializer = Expense_serializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def expense_create(request):
    serializer = Expense_serializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['is_expense'] == 'Expense':
            serializer.validated_data['amount'] *= -1
            print(serializer.validated_data)
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def expense_update(request, pk):
    expense_to_update = Expenses_model.objects.get(id=pk)
    serializer = Expense_serializer(instance=expense_to_update,
                                    data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def expense_delete(request, pk):
    expense_to_delete = Expenses_model.objects.get(id=pk)
    expense_to_delete.delete()
    return Response('deleted')

