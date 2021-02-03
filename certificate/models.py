from django.db import models
import uuid
from rest_framework import serializers
from django.dispatch import receiver
from django.db.models.signals import post_save
import urllib.request
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import StringIO
import os

from .utill import imagedraw
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

@receiver(post_save,sender=Certificate)
def img_handler(created,instance,*args,**kwargs):
    if created:
        reopen = imagedraw(instance.name)
        tempfile_io = StringIO()
        reopen.save(tempfile_io,format='JPEG')
        length=tempfile_io.seek(0, os.SEEK_END)
        image_file = InMemoryUploadedFile(tempfile_io, None, '{instance.name}.jpg','image/jpeg',str(length), None)
        #img_file = File(reopen)
        instance.image.save("{instance.name}.jpeg", image_file)
        instance.save()