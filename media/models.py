from django.db import models
from reports.models import Report


# Create your models here.
class Media(models.Model):
    file = models.FileField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True)
    report = models.ForeignKey(Report, related_name='media_files', null=True)

    def clean(self):
        self.type = self.file.name.split('.')[1]

    # def __unicode__(self):
    #     return '%s' % self.file
    #
    # def __str__(self):
    #     return self.file


""""""
