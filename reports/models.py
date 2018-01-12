from django.db import models

from witness.models import Witness


class Report(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    witness = models.ForeignKey(Witness, related_name='reports', null=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title


""""""
