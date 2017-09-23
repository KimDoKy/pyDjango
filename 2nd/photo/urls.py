from django.conf.urls import url
from photo.views import *

urlpatterns = [
    # ex: /
    url(r'^$', AlbumLV.as_view(), name='index'),

    # ex: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

    # ex: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

    # ex: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),

    # ex: /album/add/
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name='album_add'),

    # ex: /album/change/
    url(r'^album/change/$', AlbumChangeLV.as_view(), name='album_change'),

    # ex: /album/99/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$', AlbumPhotoUV.as_view(), name='album_update'),

    # ex: /album/99/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDeleteView.as_view(), name='album_delete'),

    # ex: /photo/add/
    url(r'^photo/add/$', PhotoCreateView.as_view(), name='photo_add'),

    # ex: /photo/change/
    url(r'^photo/change/$', PhotoChangeLV.as_view(), name='photo_change'),

    # ex: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$', PhotoUpdateView.as_view(), name='photo_update'),

    # ex: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', PhotoDeleteView.as_view(), name='photo_delete'),
]