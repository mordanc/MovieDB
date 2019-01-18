from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Movie, Tag, Actor

# Create your views here.
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