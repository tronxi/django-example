from rest_framework import serializers

from movies.persistence.movie import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary', 'isWatched']
