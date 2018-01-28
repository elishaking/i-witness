from django.db import models
from iwitness.settings import MEDIA_ROOT

import base64
import random
import string

from reports.models import Report


# Create your models here.
class Media(models.Model):
    file = models.TextField(blank=True)  # FileField(blank=True, null=True)
    filename = models.CharField(max_length=200)
    type = models.CharField(max_length=20, blank=True)
    report = models.ForeignKey(Report, related_name='media_files', null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        while Media.objects.filter(filename=self.filename).exists():
            self.change_file_name()

        self.type = 'image'  # FIXME: change

        data = str(self.file).replace('data:image/jpeg;base64,', '').encode()
        print(MEDIA_ROOT + "/" + self.type + "s/" + self.filename)
        self.file = "/media/" + self.type + "s/" + self.filename

        with open(MEDIA_ROOT + "/" + self.type + "s/" + self.filename, "wb") as fh:
            fh.write(base64.decodebytes(data))

        super(Media, self).save()

    def __unicode__(self):
        return '%s' % 'media'

    def __str__(self):
        return 'media'

    def change_file_name(self):
        parts = str(self.filename).split('.')
        self.filename = parts[0] + "".join([random.choice(string.ascii_letters) for _ in range(5)]) + "." + parts[1]


""""""
