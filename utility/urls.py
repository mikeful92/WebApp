__author__ = 'Mike'

from django.conf.urls import patterns, url
from utility import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^lookup/$', views.lookup, name='lookup'),
                       url(r'^results/$', views.results, name='results'),
                       )


