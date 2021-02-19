from django.conf import settings


def track_to_dto(track):
    creation_date_iso = "" if (track.creation_date is None) else track.creation_date.isoformat()
    return dict(
        id=track.id,
        link=settings.AUDIO_URL + str(track.link),
        name=track.name,
        description=track.description,
        creationDate=creation_date_iso,
        isActive=track.is_active)


def picture_to_dto(picture):
    creation_date_iso = "" if (picture.creation_date is None) else picture.creation_date.isoformat()
    return dict(
        id=picture.id,
        link=settings.IMAGE_URL + str(picture.link),
        description=picture.description,
        creationDate=creation_date_iso,
        isActive=picture.is_active
    )


def text_type_to_dto(text_type):
    return dict(
        id=text_type.id,
        name=text_type.name,
        isActive=text_type.is_active
    )


def text_to_dto(text):
    creation_date_iso = "" if (text.creation_date is None) else text.creation_date.isoformat()
    return dict(
        id=text.id,
        value=text.value,
        textType=text.text_type.name,
        creationDate=creation_date_iso,
        isActive=text.is_active
    )