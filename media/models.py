from django.db import models
from iwitness.settings import MEDIA_ROOT

import base64

from reports.models import Report


# Create your models here.
class Media(models.Model):
    file = models.CharField(max_length=10**200, blank=True)  # FileField(blank=True, null=True)
    # type = models.CharField(max_length=20, blank=True)
    # report = models.ForeignKey(Report, related_name='media_files', null=True)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.type = self.file.name.split('.')[-1]
    #     super(Media, self).save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        data = str(self.file).replace('data:image/jpeg;base64,', '').encode()
        print(self.file[0:30])
        # with open(MEDIA_ROOT + "/img.jpeg", "wb") as fh:
        #     fh.write(base64.decodebytes(data))

    def __unicode__(self):
        return '%s' % 'media'

    def __str__(self):
        return 'media'


""""""
