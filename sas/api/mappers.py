def track_to_dto(track):
    return dict(
        link=track.link,
        name=track.name,
        description=track.description,
        creationDate=track.creation_date.isoformat(),
        isActive=track.is_active)


def text_type_to_dto(text_type):
    return dict(
        name=text_type.name,
        isActive=text_type.is_active
    )


def text_to_dto(text):
    return dict(
        value=text.value,
        textType=text.text_type.name,
        creationDate=text.creation_date.isoformat(),
        isActive=text.is_active
    )
