from django.db import models


# Create your models here.
class Media(models.Model):
    file = models.FileField()
    type = models.CharField(max_length=20, blank=True)

    def clean(self):
        self.type = self.file.name.split('.')[1]

    # def __unicode__(self):
    #     return '%s' % self.file
    #
    # def __str__(self):
    #     return self.file


""""""
