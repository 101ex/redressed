from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.om_oss, name='om_oss'),
]