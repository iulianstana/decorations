import base64

from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=40)
    pozition = models.IntegerField()

    def __unicode__(self):
        return self.name

def upload_handler(instance, filename):
    return base64.b64encode('%d%s' % (Image.objects.count(), filename))


class Image(models.Model):
    titlu = models.CharField(max_length=40)
    descriere = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_handler)
    category = models.ForeignKey(Category)

    @property
    def fetch_url(self):
        # see upload_handler
        return "%s%s" % (settings.MEDIA_URL, self.file.name)

    def __unicode__(self):
        return self.titlu

# Create your models here.
