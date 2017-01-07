from django.db import models
from django.core.urlresolvers import reverse

class Person(models.Model):
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('images_person_detail', kwargs={'pk': self.pk})
