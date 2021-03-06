from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import haystack
handler404 = 'views.handler404'

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^topics/$', views.view_topics, name='view_topics'),
    url(r'^topics-list/$', views.topics_list, name='topics_list'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.topic_content, name='topic'),
    url(r'^topics/(?P<pk>[0-9]+)/new_thread$', views.new_thread, name='new_thread'),
    url(r'^tags$', views.tags, name='tags'),
    url(r'^topics/(?P<pk>[0-9]+)/threads$', views.threads, name='threads'),
    url(r'^search_tag/(?P<pk>[0-9]+)$', views.search_tag, name='search_tag'),
    url(r'^topics/(?P<par>[0-9]+)/threads/(?P<pk>[0-9]+)$', views.thread, name='thread'),
    url(r'^api/counter\.json', views.counter),
    url(r'^search$', views.search, name='search'),
    url(r'^api/comments\.json', views.get_comments),
    url(r'^api/post_comment\.json', views.new_comment),
    #url(r'^blocked$', views.get_comments),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
# url(r'^forum/$', views.post_list, name='post_list'),
# url(r'^forum/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
# url(r'^forum/post/new/$', views.post_new, name='post_new'),
# url(r'^forum/(?P<pk>[0-9]+)$', views.post_remove, name='post_remove'),
# url(r'^forum/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
"""
