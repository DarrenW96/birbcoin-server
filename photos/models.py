from django.db import models


class Photo(models.Model):
    pic = models.CharField(max_length=20)


