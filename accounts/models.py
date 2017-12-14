from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
import os

from django.urls import reverse
# Create your models here.


class User(AbstractUser):

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=10, choices=GENDERS, default=GENDERS[1][0])
    phone_number = models.IntegerField(blank=False)
    image = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.first_name

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        try:
            db_file = User.objects.all()
            if db_file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(db_file.image))
        except:
            pass
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'pk': self.pk})

