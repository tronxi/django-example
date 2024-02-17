from rest_framework.response import Response
from rest_framework.views import APIView

from movies.persistence.movie_serializer import MovieSerializer
from movies.use_cases.retrieve_movies_use_case import RetrieveMoviesUseCase


class MovieAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retrieveMoviesUseCase = RetrieveMoviesUseCase()

    def get(self, request, pk):
        movie = self.retrieveMoviesUseCase.retrieveById(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class MovieListAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.retrieveMoviesUseCase = RetrieveMoviesUseCase()

    def get(self, request):
        movies = self.retrieveMoviesUseCase.retrieveAll()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
