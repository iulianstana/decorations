import base64

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    pozition = models.IntegerField()

    def __unicode__(self):
        return self.name

def upload_handler(instance, filename):
    return 'frontend/static/img/%s' % base64.b64encode('%d%s' % (Image.objects.count(), filename))


class Image(models.Model):
    titlu = models.CharField(max_length=40)
    descriere = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_handler)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.titlu

# Create your models here.
