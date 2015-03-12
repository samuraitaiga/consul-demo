from django.conf.urls import patterns, url

from sayhost import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
