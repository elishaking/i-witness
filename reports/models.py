from django.db import models

from geopy.geocoders import Nominatim

from witness.models import Witness


class Report(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)
    witness = models.ForeignKey(Witness, related_name='reports', null=True)
    resolved = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        loc = str(self.location).split(',')
        self.location = str(Nominatim().reverse('{0}, {1}'.format(loc[0], loc[1])))
        super(Report, self).save()

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title


""""""
