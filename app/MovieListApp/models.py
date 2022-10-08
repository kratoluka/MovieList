from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100, blank=True, null=True)  # save empty string if empty or None
    description = models.CharField(max_length=1000, blank=True, null=True)
    icon_url = models.CharField(max_length=200)
    manifest_url = models.CharField(max_length=200)
    disabled = models.BooleanField()
    is_featured = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)  # generate timestamp when creating entry

    def __str__(self):
        return self.name
