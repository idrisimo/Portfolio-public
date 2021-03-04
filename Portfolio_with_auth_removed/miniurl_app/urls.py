from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'miniurl_app'
urlpatterns = [
    path('miniurl_shortener/', views.urlshortener_view, name='minishort'),
    path('miniurl/<urlend>', views.checkurl, name='mini'),
]
