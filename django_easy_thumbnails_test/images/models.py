from django.db import models
from django.core.urlresolvers import reverse

from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)

class Person(models.Model):
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('images_person_detail', kwargs={'pk': self.pk})
