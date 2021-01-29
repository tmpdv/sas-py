import os
from django.http import HttpResponse
from django.conf import settings


def get_audio(request, link):
    audio = open(os.path.join(settings.AUDIO_ROOT, link), "rb").read()
    return HttpResponse(audio, content_type="audio/mpeg")


def get_image(request, link):
    audio = open(os.path.join(settings.IMAGE_ROOT, link), "rb").read()
    return HttpResponse(audio, content_type="image/jpeg")
