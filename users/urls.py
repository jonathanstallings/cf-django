from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^/add/$', views.AddView, name='add'),
    url(r'^(?P<user_id>\d+)$', views.DetailView, name='detail'),
    url(r'^(?P<user_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<user_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^/about/$', views.about, name='about'),
]
