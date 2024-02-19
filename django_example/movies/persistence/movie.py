from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    summary = models.TextField()
    isWatched = models.BooleanField(default=False)