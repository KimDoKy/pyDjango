from django.conf.urls import url
from blog.views import *

urlpatterns = [
    # EX: /
    url(r'^$', PostLV.as_view(), name='index'),

    # Ex: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Ex: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)$', PostDV.as_view(), name='post_detail'),

    # Ex: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Ex: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Ex: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Ex: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Ex: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # Ex: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    # Ex: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    # Ex: /search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # Ex: /add/
    url(r'^add/$', PostCreateView.as_view(), name="add",),

    # Ex: /change/
    url(r'^change/$', PostChangeLV.as_view(), name="change",),

    # Ex: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update",),

    # Ex: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete",),
]