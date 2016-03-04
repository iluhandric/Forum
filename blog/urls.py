from django.conf.urls import include, url
from . import views
from django.conf.urls import patterns, url, include


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/(?P<pk>[0-9]+)$', views.post_remove, name='post_remove'),
    url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]
"""
user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

post_urls = patterns('',
    url(r'^/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

photo_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls)),
    url(r'^photos', include(photo_urls)),
)
"""