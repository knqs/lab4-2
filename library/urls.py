#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^addbook$',"mylib.views.index"),
    url(r'^addauthor$',"mylib.views.addauthor"),
    url(r'^$',"mylib.views.search"),
    url(r'^show/(?P<id>\d+)$',"mylib.views.showdetails"),
    url(r'^changebook$',"mylib.views.changebook"),
)
