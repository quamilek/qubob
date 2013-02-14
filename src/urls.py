#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from example.views import HomeView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^examples/', include('example.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
