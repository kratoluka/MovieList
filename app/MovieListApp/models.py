from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    icon_url = models.CharField(max_length=200)
    manifest_url = models.CharField(max_length=200)
    disabled = models.BooleanField()

    def __str__(self):
        return self.name
