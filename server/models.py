import base64

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    pozition = models.IntegerField()


def upload_handler(instance, filename):
    return base64.b64encode('%d%s' % (Image.object.count(), filename))


class Image(models.Model):
    titlu = models.CharField(max_length=40)
    descriere = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_handler)
    category = models.ForeignKey(Category)


# Create your models here.
