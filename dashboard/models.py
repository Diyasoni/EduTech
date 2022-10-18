from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from datetime import datetime
# Create your models here.

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Notes"
        verbose_name_plural="Notes"

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    is_finished=models.BooleanField(default=False)
    def __str__(self):
        return self.title
