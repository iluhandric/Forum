from django.conf.urls import include, url
from . import views
from django.conf.urls import patterns, url, include
#import ..mysite.settings as settings

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.view_topics, name='view_topics'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/(?P<pk>[0-9]+)$', views.post_remove, name='post_remove'),
    url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^topic/(?P<pk>[0-9]+)/$', views.topic, name='topic'),
    url(r'^thread/(?P<pk>[0-9]+)/$', views.thread, name='thread')]

