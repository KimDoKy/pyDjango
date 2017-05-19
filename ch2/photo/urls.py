from django.conf.urls import url
from photo.views import *

from photo.models import Album, Photo

urlpatterns = [
    # Ex: /
    url(r'^$', AlbumLV.as_view(model=Album), name='index'),

    # Ex: /album/, smae as /
    url(r'^album/$', AlbumLV.as_view(model=Album), name='album_list'),

    # Ex: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(model=Album), name='album_detail'),

    # Ex: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(model=Photo), name='photo_detail'),

    # Ex: /album/add/
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name="album_add"),

    # Ex: /album/change/
    url(r'^album/change/$', AlbumChangeLV.as_view(), name="album_change"),

    # Ex: /album/99/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$', AlbumPhotoUV.as_view(), name="album_update"),

    # Ex: /album/99/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDeleteView.as_view(), name="album_delete"),

    # Ex: /photo/add/
    url(r'^photo/add/$', PhotoCreateView.as_view(), name="photo_add"),

    # Ex: /photo/change/
    url(r'^photo/change/$', PhotoChangeLV.as_view(), name="photo_change"),

    # Ex: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$', PhotoUpdateView.as_view(), name="photo_update"),

    # Ex: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', PhotoDeleteView.as_view(), name="photo_delete"),
]