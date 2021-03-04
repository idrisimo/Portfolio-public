from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'expensetracker_app'
urlpatterns = [
    path('expensetracker/', views.expensedashboard_view, name='dashboard'),

    path('apiview/', views.apiOverview, name='api-overview'),
    path('expense-list/', views.expense_list, name='expense-list'),
    path('expense-create/', views.expense_create, name='expense-create'),
    path('expense-update/<str:pk>/', views.expense_update, name='expense-update'),
    path('expense-delete/<str:pk>/', views.expense_delete, name='expense-delete'),

]
