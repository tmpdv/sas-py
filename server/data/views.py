from .models import *
from django.http import HttpResponse
from .mappers import to_dto_mapper
from .mappers import to_page_mapper

import json


def tracks(request):
    track_models = Track.objects.filter(is_active=True).order_by('-creation_date')
    tracks_mapped = list()

    for t in track_models:
        tracks_mapped.append(to_dto_mapper.track_to_dto(t))

    tracks_json = json.dumps(to_page_mapper.to_first_page_default_size(tracks_mapped), ensure_ascii=False)
    return HttpResponse(tracks_json, content_type="text/json")


def pictures(request):
    picture_models = Picture.objects.filter(is_active=True).order_by('-creation_date')
    pictures_mapped = list()

    for p in picture_models:
        pictures_mapped.append(to_dto_mapper.picture_to_dto(p))

    pictures_json = json.dumps(to_page_mapper.to_first_page_default_size(pictures_mapped), ensure_ascii=False)
    return HttpResponse(pictures_json, content_type="text/json")


def texts(request):
    text_models = Text.objects.filter(is_active=True).order_by('-creation_date')
    texts_mapped = list()

    for t in text_models:
        texts_mapped.append(to_dto_mapper.text_to_dto(t))

    texts_json = json.dumps(to_page_mapper.to_first_page_default_size(texts_mapped), ensure_ascii=False)
    return HttpResponse(texts_json, content_type="text/json")


def track(request, track_id):
    track_model = Track.objects.get(id=track_id)
    track_json = json.dumps(to_dto_mapper.track_to_dto(track_model), ensure_ascii=False)
    return HttpResponse(track_json, content_type="text/json")


def picture(request, picture_id):
    picture_model = Picture.objects.get(id=picture_id, is_active=True)
    picture_json = json.dumps(to_dto_mapper.picture_to_dto(picture_model), ensure_ascii=False)
    return HttpResponse(picture_json, content_type="text/json")


def text(request, text_id):
    text_model = Text.objects.get(id=text_id)
    text_json = json.dumps(to_dto_mapper.text_to_dto(text_model), ensure_ascii=False)
    return HttpResponse(text_json, content_type="text/json")


def about(request):
    text_type_model = TextType.objects.get(id=1)
    text_model = Text.objects.get(text_type=text_type_model)
    text_json = json.dumps(to_dto_mapper.text_to_dto(text_model), ensure_ascii=False)
    return HttpResponse(text_json, content_type="text/json")