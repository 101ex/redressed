from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

def sortiment(request):
    context = {
    }
    template = loader.get_template('shop/base_Sortiment.html')
    return HttpResponse(template.render(context, request))