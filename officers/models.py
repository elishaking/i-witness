from django.db import models

from accounts.models import User
# Create your models here.


class Officer(models.Model):
    account = models.ForeignKey(User, related_name='officers')
    id = models.CharField(primary_key=True, max_length=30, help_text='Enter unique Police id')
    activity = models.CharField(max_length=200)
