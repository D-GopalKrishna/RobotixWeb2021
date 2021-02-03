from django.db import models
import uuid
from rest_framework import serializers

# Create your models here.
class Event(models.Model):
    content = models.TextField()
    date_event = models.DateField()
    date_result = models.DateField()
    sign = models.ImageField(upload_to='signature/')

class Certificate(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url_key = models.UUIDField(default=uuid.uuid4,unique=True,auto_created=True)
    image = models.ImageField(upload_to='certificate/',null=True,blank=True)
