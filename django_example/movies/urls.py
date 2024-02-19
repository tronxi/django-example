from django.urls import path

from django_example.movies.api.movie_api_view import MovieAPIView, MovieListAPIView

urlpatterns = [
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<int:pk>/', MovieAPIView.as_view()),
]
