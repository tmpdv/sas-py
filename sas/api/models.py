from django.db import models


# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=128, unique=True)
    link = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, default='')
    creation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Track[name={self.name}, link='{self.link}', creation_date={self.creation_date}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"


class TextType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"TextType[name={self.name}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"


class Text(models.Model):
    title = models.CharField(max_length=100)
    value = models.TextField(blank=True)
    text_type = models.ForeignKey(TextType, on_delete=models.CASCADE)
    creation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Text[title={self.title}, type={self.text_type.name}, " \
               f"creation_date={self.creation_date}, " \
               + ("ACTIVE" if self.is_active else "NOT ACTIVE") + "]"
