from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

from iwitness.settings import MEDIA_ROOT

import base64


class User(AbstractUser):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=GENDERS, default=GENDERS[1][0], blank=True)
    phone_number = models.IntegerField()  # FIXME: MAKE UNIQUE
    image = models.CharField(max_length=10**20, blank=True)

    def __unicode__(self):
        return '%s' % self.username

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save()
        if self.image:
            print(self.image)
            data = str(self.image).replace('data:image/jpeg;base64,', '').encode()
            filename = User.objects.filter(phone_number=self.phone_number).pk
            print(filename)
            with open(MEDIA_ROOT + "/account_avatar/" + filename, "wb") as fh:
                fh.write(base64.decodebytes(data))

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'pk': self.pk})


""""""
