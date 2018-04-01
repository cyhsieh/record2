from django.shortcuts import render
from movies.models import Genre
from movies.models import Director
from movies.models import Actor
from movies.models import Movie, RATING_CHOICES
from movies.forms import MovieFilterForm
# Create your views here.

def movie_base(request):
    return render(request, "movies/base_two_columns.html", locals())

def movie_list(request):
    qs = Movie.objects.order_by('title')

    #form =  MovieFilterForm(request.REQUEST)
    form =  MovieFilterForm()

    facets = {
            'selected':{},
            'categories':{
                'genres':Genre.objects.all(),
                'directors':Director.objects.all(),
                'actors':Actor.objects.all(),
                'ratings':RATING_CHOICES,
            },
    }
    if form.is_valid():
        genre = form.cleaned_data['gnere']
        if genre:
            facets['selected']['genre'] = genre
            qs = qs.filter(genres=genre).distinct()
        director = form.cleaned_data['director']
        if director:
            facets['selected']['director'] = director
            qs = qs.filter(directors=director).distinct()
        actor = form.cleaned_data['actor']
        if actor:
            facets['selected']['actor'] = actor
            qs = qs.filter(actors=actor).distinct()
        rating = form.cleaned_data['rating']
#        if rating:
#            facets['selected']['rating'] = \(int(rating),dict(RATING_CHOICES)[int(rating)])
#            qs = qs.filter(ratings=rating).distinct()
    context = {
            'form':form,
            'facets':facets,
            'object_list':qs,
    }
    return render(request, "movies/movie_list.html", context)




