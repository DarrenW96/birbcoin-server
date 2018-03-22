from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^photos/', include('photos.urls')),
    url(r'^register/', views.register, name='register'),
]
