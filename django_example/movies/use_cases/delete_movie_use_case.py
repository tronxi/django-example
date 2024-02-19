from django.http import Http404

from django_example.movies.persistence.movie import Movie


class DeleteMovieUseCase:

    def deleteById(self, id):
        try:
            movie = Movie.objects.get(pk=id)
            print("deleting")
            movie.delete()
        except Movie.DoesNotExist:
            raise Http404
