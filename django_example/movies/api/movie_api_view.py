from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django_example.movies.persistence.movie_serializer import MovieSerializer
from django_example.movies.use_cases.delete_movie_use_case import DeleteMovieUseCase
from django_example.movies.use_cases.retrieve_movies_use_case import RetrieveMoviesUseCase
from django_example.users.permissions.is_admin_permission import IsAdminPermission


class MovieAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retrieveMoviesUseCase = RetrieveMoviesUseCase()
        self.deleteMovieUseCase = DeleteMovieUseCase()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsAdminPermission()]
        else:
            return [IsAuthenticated()]

    def get(self, request, pk):
        movie = self.retrieveMoviesUseCase.retrieveById(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk):
        self.deleteMovieUseCase.deleteById(pk)
        return Response()


class MovieListAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retrieveMoviesUseCase = RetrieveMoviesUseCase()

    def get(self, request):
        movies = self.retrieveMoviesUseCase.retrieveAll()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
