from django.conf.urls import url
from blog.views import *

urlpatterns = [
    # ex: /
    url(r'^$', PostLV.as_view(), name='index'),

    # ex: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # ex: /post/ex/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # ex: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # ex: /2017/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # ex: /2017/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # ex: /2017/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # ex: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    # ex: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    # ex: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    # ex: /search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # ex: /add/
    url(r'^add/$', PostCreateView.as_view(), name="add"),

    # ex: /change/
    url(r'^change/$', PostChangeLV.as_view(), name="change"),

    # ex: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update"),

    # ex: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete"),

    # ex: /test/
    url(r'^test/$', TestPostLV.ad_view(), name='post_test'),

    # ex: /test/word/
    url(r'^test/(?P<word>[\w]+)/$', TestPostLV.as_view(), name='post_test'),
]