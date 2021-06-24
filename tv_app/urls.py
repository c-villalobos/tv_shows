from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<show_id>', views.details),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/delete', views.delete),
]