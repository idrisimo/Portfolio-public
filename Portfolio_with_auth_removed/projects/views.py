from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project

def home_view(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    response = render(request, 'home.html', context)
    response.set_cookie(key='cross-site-cookie', value='bar', samesite='Strict')
    return response

def about_view(request):
    context = {}
    return render(request, 'about.html', context)

@api_view(['POST', 'GET'])
def contact_email(request):
    email_data = request.data
    print(email_data)
    send_mail(from_email='idrissilvaportfolio@outlook.com',
              subject=f'Portfolio contact message from: {email_data["name"]}',
              message=f'Senders email: \n'
                      f'{email_data["email_address"]}\n\n'
                      f'Please see message below: \n'
                      f'{email_data["comment"]}',
              recipient_list=['idrissilva@hotmail.com'])
    return Response('email_sent')


def read_file(request):
    f = open('.well-known/pki-validation/1997B10AD4CDF2D181ED1A918571969E.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")