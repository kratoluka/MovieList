from django.shortcuts import render
from .models import Movie
from datetime import datetime, timedelta


def index(request):
    # sort and filter options list to pass to html
    # key for value that is passed back
    # value for text that is displayed
    sort_options = {
        'date_added': 'Date added',
        'name': 'Name',
        'is_featured': 'Featured'
    }
    filter_options = {
        '': 'None',
        'is_featured': 'Featured',
        'new_this_week': 'This week',
        'new_this_month': 'This month',
        'new_this_year': 'This year'
    }

    # get current sort and filter
    sort = request.GET.get('sort', 'date_added')
    filt = request.GET.get('filter', '')

    # load movie list
    movie_list = Movie.objects.all()

    if sort:
        if sort == 'is_featured':  # is_featured has to be sorted in reverse
            movie_list = movie_list.order_by('-is_featured')
        else:
            movie_list = movie_list.order_by(sort)

    if filt:
        now = datetime.now()
        if filt == 'is_featured':
            movie_list = movie_list.filter(is_featured=True)
        elif filt == 'new_this_week':  # filter by date using range
            movie_list = movie_list.filter(date_added__range=[now - timedelta(days=7), now])
        elif filt == 'new_this_month':
            movie_list = movie_list.filter(date_added__range=[now - timedelta(days=30), now])
        elif filt == 'new_this_year':
            movie_list = movie_list.filter(date_added__range=[now - timedelta(days=365), now])

    context = {
        'movie_list': movie_list,
        'sort': sort,
        'filter': filt,
        'sort_options': sort_options,
        'filter_options': filter_options
    }

    return render(request, 'index.html', context)
