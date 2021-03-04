from django.urls import path

from . import views

app_name = 'reddit_app'
urlpatterns = [
    path('timetopost/', views.timetopost_view, name='timetopost'),

    path('timetopost/collectdata/', views.collect_reddit_data, name='collectdata'),
    path('timetopost/showdata/', views.show_reddit_data, name='showdata'),
]