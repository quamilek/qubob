#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib import admin
from example.models import Book


class BookAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'pub_date', 'price')
admin.site.register(Book, BookAdmin)
