from django.http import HttpResponse
from .models import Track, Text
from .mappers import track_to_dto, text_to_dto
import json


# Create your views here.
def tracks(request):
    tracks_model = Track.objects.filter(is_active=True).order_by('-creation_date')
    tracks_dto = list()
    for t in tracks_model:
        tracks_dto.append(track_to_dto(t))
    tracks_json = json.dumps(tracks_dto, ensure_ascii=False)
    return HttpResponse(tracks_json, content_type="text/json")


def texts(request):
    texts_model = Text.objects.filter(is_active=True).order_by('-creation_date')
    texts_dto = list()
    for t in texts_model:
        texts_dto.append(text_to_dto(t))
    texts_json = json.dumps(texts_dto, nsure_ascii=False)
    return HttpResponse(texts_json, content_type="text/json")
