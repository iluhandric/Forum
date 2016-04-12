from django.conf.urls import include, url
from . import views
from django.conf.urls import patterns, url, include
#import ..mysite.settings as settings
from django.conf import settings
from django.conf.urls.static import static



handler404 = 'views.handler404'

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.view_topics, name='view_topics'),
    url(r'^ask/$', views.ask, name='ask'),
    # url(r'^blog/$', views.post_list, name='post_list'),
    # url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^blog/post/new/$', views.post_new, name='post_new'),
    # url(r'^blog/(?P<pk>[0-9]+)$', views.post_remove, name='post_remove'),
    # url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.topic, name='topic'),
    url(r'^topics/(?P<pk>[0-9]+)/tags$', views.tags, name='tags'),
    url(r'^topics/(?P<pk>[0-9]+)/threads$', views.threads, name='threads'),
    url(r'^topics/(?P<par>[0-9]+)/search/(?P<pk>[0-9]+)$', views.search_tag, name='search_tag'),
    url(r'^topics/(?P<par>[0-9]+)/threads/(?P<pk>[0-9]+)$', views.thread, name='thread'),
 #   url(r'^admin_entering', views.admin_login, name='admin_login'),
#    url(r'^block_user', views.block_user, name='block_user'),
    url(r'^resources(?P<img>.*)$', views.image_original, name='original'),
    url(r'^api/counter\.json', views.counter),
    url(r'^api/comments\.json', views.get_comments),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

