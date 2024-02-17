from django.http import Http404

from movies.persistence.movie import Movie


class RetrieveMoviesUseCase:
    def retrieveAll(self):
        movies = Movie.objects.all()
        for movie in movies:
            print(movie)
        return movies


    def retrieveById(self, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404
        print(movie)
        return movie
