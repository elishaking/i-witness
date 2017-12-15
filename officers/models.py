from django.db import models

from accounts.models import User

from django.conf import settings
import os

from django.urls import reverse
# Create your models here.


class Officer(models.Model):
    account = models.ForeignKey(User, related_name='officers')
    id = models.CharField(primary_key=True, max_length=30, help_text='Enter unique Police id')
    activity = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.account

    def __str__(self):
        return self.account

    def save(self, *args, **kwargs):
        try:
            db_file = Officer.objects.all()
            if db_file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(db_file.image))
        except:
            pass
        super(Officer, self).save(*args, **kwargs)





