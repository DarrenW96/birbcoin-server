from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^gallery$', views.gallery, name='gallery'),
	url(r'^gallery2$', views.gallery2, name='gallery2'),
	url(r'^gallery2a$', views.gallery2a, name='gallery2a'),
]
