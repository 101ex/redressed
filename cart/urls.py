from django.conf.urls import include, url

urlpatterns = [
    #this pattern must always be the last
    url('', include('easycart.urls'))
]