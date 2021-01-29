from django.urls import path
from . import views

urlpatterns = [
    path('audio/<str:link>', views.get_audio, name="get_audio"),
    path('image/<str:link>', views.get_image, name="get_image"),
]
