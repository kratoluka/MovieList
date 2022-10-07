from django.conf import settings
import requests
from .models import Movie
from datetime import datetime


def load_movie_list():
    print(20*'-')

    # fetch movie list from source
    response = requests.get(settings.MOVIE_LIST_SOURCE)

    if response.status_code != 200:  # if request failed
        print(f'Error {response.text}')
        return

    data = response.json()

    print(datetime.now())
    for mov in data:
        print(mov['name'])
        Movie.objects.update_or_create(
            name=mov['name'],
            short_name=mov['shortName'],
            description=mov['description'],
            icon_url=mov['iconUri'],
            manifest_url=mov['manifestUri'],
            disabled=mov['disabled'],
            is_featured=mov['isFeatured']
        )
