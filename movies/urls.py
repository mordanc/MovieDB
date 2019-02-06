from django.urls import path
from movies.views import HomepageView

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieIndexView.as_view(), name='movie_index'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('tags/', views.TagIndexView.as_view(), name='tag_index'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('search_results/', views.SearchResults, name='search_results'),
    path('homepage/', views.HomepageView, name='homepage'),
]