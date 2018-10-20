from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    followers = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')