import os
from django.http import HttpResponse
from django.conf import settings
from .forms import UploadFileForm


def get_audio(request, link):
    audio = open(os.path.join(settings.AUDIO_ROOT, link), "rb").read()
    return HttpResponse(audio, content_type="audio/mpeg")


def get_image(request, link):
    audio = open(os.path.join(settings.IMAGE_ROOT, link), "rb").read()
    return HttpResponse(audio, content_type="image/jpeg")


def upload_audio(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("success")
    else:
        return HttpResponse("fail")


def handle_uploaded_file(f):
    with open(os.path.join(settings.AUDIO_ROOT, "new_track.mp3"), 'rb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
