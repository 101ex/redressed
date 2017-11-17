from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

def index(request):
    context = {
        #grab articles from database
    }
    template = loader.get_template('news/base_index.html')
    html = template.render(context, request)
    return HttpResponse(html)