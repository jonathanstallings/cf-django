from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^/add/$', views.AddView, name='add'),
]
