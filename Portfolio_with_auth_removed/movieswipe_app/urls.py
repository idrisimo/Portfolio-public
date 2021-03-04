from django.urls import path

from . import views

app_name = 'reddit_app'
urlpatterns = [
    path('movieswipe/party', views.movieswipe_view, name='movieswipe'),
    path('movieswipe/', views.landing_view, name='landing_page'),
    path('login/movieswipe/', views.login_view, name='movieswipe_login'),
    path('register/movieswipe/', views.register_view, name='movieswipe_register'),

    path('movieswipe/host_party/', views.host_party, name='host_party'),
    path('movieswipe/join_party/', views.join_party, name='join_party'),

    path('movie-apiview/', views.apiOverview, name='api-overview'),
    path('movie-list/', views.movie_list, name='movie-list'),
    path('movie-detail/<str:pk>/', views.movie_detail, name='movie-detail'),
    path('movie-create/', views.movie_create, name='movie-create'),
    path('movie-update/<str:pk>/', views.movie_update, name='movie-update'),
    path('movie-delete/<str:pk>/', views.movie_delete, name='movie-delete'),
]