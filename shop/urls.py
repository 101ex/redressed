from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sortiment, name='sortiment'),
    #dynamic page depending on database tables
    #url(r'^[1-*]$'
]
