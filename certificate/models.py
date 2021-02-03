from django.db import models
import uuid
from rest_framework import serializers
from django.dispatch import receiver
from django.db.models.signals import post_save
import urllib.request
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
import os

from .utill import imagedraw
from events.models import Event
# Create your models here.

class Certificate(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url_key = models.UUIDField(default=uuid.uuid4,unique=True,auto_created=True)
    image = models.ImageField(upload_to='certificate/',null=True,blank=True)

@receiver(post_save,sender=Certificate)
def img_handler(created,instance,*args,**kwargs):
    if created:
        reopen = imagedraw(instance.name)
        tempfile_io = io.BytesIO()
        reopen.save(tempfile_io,format='JPEG')
        #length=tempfile_io.seek(0, os.SEEK_END)
        instance.image = InMemoryUploadedFile(tempfile_io, None, '{instance.name}.jpg','image/jpeg',tempfile_io.tell, None)
        #img_file = File(reopen)
        #.save("{instance.name}.jpeg", image_file)
        instance.save()