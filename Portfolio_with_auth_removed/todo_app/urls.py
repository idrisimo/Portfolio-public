from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('todolist/', views.todo_view, name='todo'),
    path('apiview/', views.apiOverview, name='api-overview'),
    path('todo-list/', views.todoList, name='todo-list'),
    path('todo-detail/<str:pk>/', views.todoDetail, name='todo-detail'),
    path('todo-create/', views.todoCreate, name='todo-create'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='todo-update'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todo-delete'),

    path('sms/todo-control/', views.sms_controller, name='sms_api'),
    path('pincode/', views.pincode, name='pincode'),
    path('mobile/', views.mobile_grabber, name='mobile'),
]
