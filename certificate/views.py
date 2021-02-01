from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Certificate

def Search(request,url_key):
    obj = get_object_or_404(Certificate,url_key=url_key)
    return HttpResponse("Certificte of = %s." % obj.name)