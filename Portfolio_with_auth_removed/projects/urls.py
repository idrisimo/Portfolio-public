from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact_api/', views.contact_email, name='contact'),
    path('.well-known/pki-validation/DC5670F57758D79366DEAB34316ACFE1.txt', views.read_file),
]
