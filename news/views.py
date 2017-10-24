from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

def index(request):
    context = {

    }
    template = loader.get_template('homepage/index.html')
    return HttpResponse(template.render(context, request))
