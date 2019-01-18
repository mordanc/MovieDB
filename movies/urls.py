from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieIndexView.as_view(), name='movie_index'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('tags/', views.TagIndexView.as_view(), name='tag_index'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
]