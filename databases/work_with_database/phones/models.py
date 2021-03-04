from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(' '.join((str(self.name), str(self.release_date))))
        super(Phone, self).save(*args, **kwargs)
