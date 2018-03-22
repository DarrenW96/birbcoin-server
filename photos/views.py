from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())
	
def gallery2(request):
    template = loader.get_template('gallery2.html')
    return HttpResponse(template.render())

def gallery2a(request):
    template = loader.get_template('gallery2a.html')
    return HttpResponse(template.render())