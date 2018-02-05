from django.shortcuts import render

from easycart import BaseCart

# Create your views here.

from shop.models import ApparelType, Apparel

class Cart(BaseCart):

    def get_queryset(self, pks):
        return Apparel.objects.filter(pk__in=pks)
