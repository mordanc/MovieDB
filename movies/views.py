from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.db.models import Q

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

class SearchResults(generic.ListView):
    paginate_by = 10
    
    def get_queryset(self):
        result = super(SearchResults, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and__,
                (Q(content__icontains=q) for q in query_list))
            )
        return result
