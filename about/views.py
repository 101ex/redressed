from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import models

def om_oss(request):
    context = {

    }
    template = loader.get_template('about/base_Om_oss.html')
    return HttpResponse(template.render(context, request))
