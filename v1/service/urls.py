from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^ratecard-cooking$', views.ratecard_cooking, name='ratecard_cooking'),
    url(r'^ratecard-house$', views.ratecard_house, name='ratecard_house'),
    url(r'^ratecard-bathroom$', views.ratecard_bathroom, name='ratecard_bathroom'),
    url(r'^ratecard-kitchen', views.ratecard_kitchen, name='ratecard_kitchen'),
]
