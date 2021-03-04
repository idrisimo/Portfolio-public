from django.urls import path

from . import views

app_name = 'language_learn'
urlpatterns = [
    path('language/', views.dashboard_view, name=''),
]