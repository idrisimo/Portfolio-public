from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .ProjectScripts import tmdb_api_wrapper as tmdb
from .ProjectScripts import aws_dynamodb_api as aws

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/movie-list/',
        'Detail View': '/movie-detail/<str:pk>/',
        'Create': '/movie-create/',
        'Update': '/movie-update/<str:pk>/',
        'Delete': '/movie-delete/<str:pk>/',
    }
    return Response(api_urls)

def movieswipe_view(request):

    context = {}
    return render(request, 'movieswipe.html', context)

@api_view(['GET'])
def movie_list(request):
    movies = Movie_details_model.objects.all()
    serializer = Movie_details_serializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    return Response()

@api_view(['POST', 'GET'])
def movie_create(request):
    print("test")
    return Response()

@api_view(['POST', 'GET'])
def movie_update(request, pk):
    return Response()

@api_view(['DELETE'])
def movie_delete(request, pk):
    return Response()


def register_view(request):
    user_creation_form = CreateUserForm()
    if request.method == 'POST':
        user_creation_form = CreateUserForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = user_creation_form.cleaned_data.get('username')
            messages.success(request, f"User has been created for {user}!")
            return redirect('login_page.html')
    context = {'user_creation_form': user_creation_form}
    return render(request, 'register.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, username)
            redirect('landing_page.html')

    context = {}
    return render(request, 'login_page.html', context)

def landing_view(request):

    context = {}
    return render(request, 'landing_page.html', context)
@api_view(['POST', 'GET'])
def host_party(request):
    party_planner = aws.Party_planner(host_key="ABCD", host_user="Steven")
    create_party = party_planner.create_party()
    if request.POST.get('click', True):
        create_party
    return Response()

@api_view(['POST', 'GET'])
def join_party(request):
    user_info = {"Juliet": {"Genre Preference": ["History"], "Release Date": "01-02-2020"}}
    party_planner = aws.Party_planner(host_key="ABCD", host_user="Steven", user_details=user_info)
    join_host = party_planner.add_party_members()
    if request.POST.get('click', True):
        join_host
    return Response(print("Party Joined"))