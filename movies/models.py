from django.db import models
from django.utils.translation import ugettext_lazy as _ 
# Create your models here.

RATING_CHOICES = (
        (1,u"✩"),
        (2,u"✩✩"),
        (3,u"✩✩✩"),
        (4,u"✩✩✩✩"),
        (5,u"✩✩✩✩✩"),
)

class Genre(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(_("First name"), max_length=40)
    last_name = models.CharField(_("Last name"), max_length=40)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Actor(models.Model):
    first_name = models.CharField(_("First name"), max_length=40)
    last_name = models.CharField(_("Last name"), max_length=40)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Movie(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    genres = models.ManyToManyField(Genre, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    def __str__(self):
        return self.title




