from django.db import models

from accounts.models import User
from reports.models import Report
# Create your models here.


class Witness(models.Model):
    account = models.OneToOneField(User, related_name='witness')
    reports = models.ForeignKey(Report, null=True)
