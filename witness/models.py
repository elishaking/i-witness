from django.db import models

from accounts.models import User

from django.conf import settings
import os

from django.urls import reverse


# Create your models here.


class Witness(models.Model):
    account = models.OneToOneField(User)

    # def __unicode__(self):
    #     return '%s' % 'witness'

    def __str__(self):
        return self.account.username


""""""
