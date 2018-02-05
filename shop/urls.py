from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?P<apparel>[\w]+)/', include([
        url(r'^$', views.sortiment, name='sortiment_apparel'),
        url(r'^(?P<apparel_id>[\d]+)/$', views.sortiment, name='sortiment_apparel_focus'),

    ])),
]