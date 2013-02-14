#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bob.menu import MenuItem
from django.views.generic import TemplateView
from settings import DOC_URL

class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        mainmenu_items = [
            MenuItem('doc', href=DOC_URL, icon='question-sign'),
            MenuItem('DataTable', view_name='data_table', icon='list-alt'),
        ]
        return {
            'section': 'home',
            'mainmenu_items': mainmenu_items,
        }


class HomeView(BaseView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        return  super(HomeView, self).get_context_data(*args, **kwargs)
