#decorators
from django.views.decorators.csrf import ensure_csrf_cookie

from django.shortcuts import render

# Create your views here.

@ensure_csrf_cookie
def checkout(request):
    context = {

    }
    return render(request, 'checkout/base_Checkout.html', context)

@ensure_csrf_cookie
def checkout_swish(request):
    context = {

    }
    return render(request, 'checkout/base_Checkout_Swish.html', context)