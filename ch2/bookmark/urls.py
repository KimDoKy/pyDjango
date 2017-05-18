from django.conf.urls import url
from bookmark.views import *

urlpatterns = [
    # Class-based views
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', BookmarkDV.as_view(), name='detail'),

    # Ex: /add/
    url(r'^add/$', BookmarkCreateView.as_view(), name="add",),

    # Ex: /change/
    url(r'^change/$', BookmarkChangeLV.as_view(), name="change",),

    # Ex: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name="update",),

    # Ex: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name="delete",),
]