from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.checkout, name='checkout'),
    url(r'^swish/$', views.checkout_swish, name='checkout_swish'),
]