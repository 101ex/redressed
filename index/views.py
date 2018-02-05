from django.shortcuts import render
from django.template import loader
from .models import Article
from . import models

def index(request):
    all_articles = Article.objects.all()

    context = {
        #grab articles from database
        "all_articles":all_articles,
    }

    return render(request, 'index/base_index.html', context)