from django.conf.urls import url
from . import views

#app_name = 'app'

urlpatterns = [
        url(r'^$', views.get_name, name = 'get_name'),
        url(r'^getname/$', views.get_name, name = 'get_name')
        ]