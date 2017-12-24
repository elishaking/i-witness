from django.db import models

from django.conf import settings
import os

from witness.models import Witness

from django.urls import reverse
# Create your models here.


class Media(models.Model):
    image = models.FileField()
    audio = models.FileField()
    video = models.FileField()

    def __unicode__(self):
        return '%s' % self.image

    def __str__(self):
        return self.image


class Report(models.Model):
    witness = models.ForeignKey(Witness, related_name='reports')
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    media = models.ForeignKey(Media)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            db_file = Report.objects.all()
            if db_file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(db_file.image))
        except:
            pass
        super(Report, self).save(*args, **kwargs)


