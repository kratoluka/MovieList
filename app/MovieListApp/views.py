from django.shortcuts import render
from .models import Movie


def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'index.html', {'movie_list': movie_list})
