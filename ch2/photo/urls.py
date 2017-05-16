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
]