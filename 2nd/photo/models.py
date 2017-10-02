from django.db import models
from django.core.urlresolvers import reverse

from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey(User, null=True)

    class Mete:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Publication(models.Model):
    title = models.CharField(max_length=30)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place)
    name = models.CharField(max_length=50, default='DefRestName')
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.name
