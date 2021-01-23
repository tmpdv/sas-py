from django.db import models

storage_url = "http://localhost:8090/store"
audio_url = "/audio"
image_url = "/image"


# Create your models here.
class Track(models.Model):
    link = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"Track[id={self.id}, name={self.name}, link='{self.link}', creation_date={self.creation_date}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"

    def as_json(self):
        creation_date_iso = "" if (self.creation_date is None) else self.creation_date.isoformat()
        return dict(
            id=self.id, link=storage_url + audio_url + str(self.link), name=self.name,
            description=self.description, creationDate=creation_date_iso, isActive=self.is_active)


class Picture(models.Model):
    link = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"Picture[id={self.id}, link='{self.link}', creation_date={self.creation_date}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"

    def as_json(self):
        creation_date_iso = "" if (self.creation_date is None) else self.creation_date.isoformat()
        return dict(
            id=self.id, link=storage_url + image_url + str(self.link), description=self.description,
            creationDate=creation_date_iso, isActive=self.is_active)


class TextType(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField()

    def __str__(self):
        return f"TextType[id={self.id}, name={self.name}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"

    def as_json(self):
        return dict(id=self.id, name=self.name, isActive=self.is_active)


class Text(models.Model):
    title = models.CharField(max_length=100)
    value = models.TextField(default="")
    text_type = models.ForeignKey(TextType, on_delete=models.CASCADE)
    creation_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"Text[id={self.id}, title={self.title}, type={self.text_type.name}, " \
               f"creation_date={self.creation_date}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"

    def as_json(self):
        creation_date_iso = "" if (self.creation_date is None) else self.creation_date.isoformat()
        return dict(
            id=self.id, value=self.value, textType=self.text_type.name,
            creationDate=creation_date_iso, isActive=self.is_active)
