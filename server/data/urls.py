from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.tracks),
    path('pictures/', views.pictures),
    path('texts/', views.texts),
    path('track/<int:track_id>', views.track, name="track"),
    path('picture/<int:picture_id>', views.picture, name="picture"),
    path('text/<int:text_id>', views.text, name="text"),
    path('about/', views.about, name="about"),
]
