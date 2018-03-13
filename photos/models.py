from django.db import models


class Photo(models.Model):
    pic = models.ImageField()


