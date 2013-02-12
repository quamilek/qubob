#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse

class View(object):

    def index(request):
        return HttpResponse("Hello, world. You're at the poll index.")