from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class register(models.Model):
    username = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

class signup(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=200)
    passw = models.CharField(max_length=20)
