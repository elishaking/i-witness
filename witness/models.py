from django.db import models

from accounts.models import User
from reports.models import Report

from django.conf import settings
import os

from django.urls import reverse
# Create your models here.


class Witness(models.Model):
    account = models.OneToOneField(User)
    # reports = models.ForeignKey(Report, null=True)

    def __unicode__(self):
        return '%s' % self.account

    def __str__(self):
        return self.account

    def save(self, *args, **kwargs):
        try:
            db_file = Witness.objects.all()
            if db_file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(db_file.image))
        except:
            pass
        super(Witness, self).save(*args, **kwargs)


