from django.db import models

# Create your models here.


class Media(models.Model):
    image = models.FileField()
    audio = models.FileField()
    video = models.FileField()


class Report(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    media = models.ForeignKey(Media)
