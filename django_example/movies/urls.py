from django.urls import path

from django_example.movies.api.movie_api_view import MovieAPIView, MovieListAPIView
from django_example.movies.consumers.movies_consumer import MoviesConsumer

urlpatterns = [
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<int:pk>/', MovieAPIView.as_view()),
]

websocket_urlpatterns = [
    path("ws/movies/", MoviesConsumer.as_asgi()),
]
