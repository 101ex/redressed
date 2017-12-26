from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Article
from . import models

def index(request):
    all_articles = Article.objects.all()

    context = {
        #grab articles from database
        "all_articles":all_articles,
    }

    template = loader.get_template('news/base_index.html')
    html = template.render(context, request)
    return HttpResponse(html)