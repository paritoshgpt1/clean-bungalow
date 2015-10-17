from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^book-service$', views.book_service, name='book_service'),
]
