from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.views.generic import TemplateView
import requests

from .models import Movie, Tag, Actor
from .forms import SearchForm

# Create your views here.
def HomepageView(request):
    response = requests.get('http://www.omdbapi.com/?apikey=a6793cf9&t=Blade+Runner&y=2017')
    moviedata = response.json()

    return render(request, 'movies/homepage.html', 
        moviedata)

class MovieIndexView(generic.ListView):
    template_name='movies/movie_index.html'
    context_object_name = 'movies_list'
    
    def get_queryset(self):
        return Movie.objects.order_by('movie_title')[:10]

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

class TagIndexView(generic.ListView):
    template_name = 'movies/tag_index.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Tag.objects.order_by('tag_name')

class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'movies/tag_detail.html'

def SearchResults(request):
    search_result = {}
    if 'search_string' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = SearchForm()
    
    return render(request, 'movies/search_results.html', {'form': form, 'search_result': search_result})
