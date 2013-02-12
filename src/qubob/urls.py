#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from example.views import ExampleView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'qubob.views.index', name='index'),
#    url(r'^example/', include('View.index')),
    url(r'^example/', ExampleView.as_view(), name='example'),


    url(r'^admin/', include(admin.site.urls)),
)
