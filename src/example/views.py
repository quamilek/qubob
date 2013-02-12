#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bob.data_table import DataTableMixin, DataTableColumn
from django.views.generic import TemplateView
from example.models import Book


class DataTableExample(DataTableColumn):
    def __init__(self, header_name, foreign_field_name=None,
                 sort_expression=None, export=None, **kwargs):
        super(DataTableExample, self).__init__(header_name, **kwargs)
        self.sort_expression = sort_expression
        self.export = export

class ExampleView(TemplateView, DataTableMixin):
    template_name = "base.html"
    sort_variable_name = 'sort'
    rows_per_page = 5
    export_variable_name = 'export'

    _ = DataTableExample
    columns = [
        _('Dropdown', selectable=True, bob_tag=True),
        _('Title', field='title', sort_expression='title', bob_tag=True),
        _('Publication Date', field='pub_date', sort_expression='pub_date', bob_tag=True),
        _('Price', field='price', sort_expression='price', bob_tag=True),
    ]


    def get_context_data(self, *args, **kwargs):
        ret = super(ExampleView, self).get_context_data(*args, **kwargs)
        ret.update(
            super(ExampleView, self).get_context_data_paginator(
                *args,
                **kwargs
            )
        )
        ret.update({
            'sort_variable_name': self.sort_variable_name,
            'url_query': self.request.GET,
            'params': 'test',
            'sort': self.sort,
            'columns': self.columns,
        })
        return ret

    def get_query(self):
        books = Book.objects.all()
        self.data_table_query(books)

    def get(self, *args, **kwargs):
        self.get_query()
        if self.export_requested():
            return self.response
        return super(ExampleView, self).get(*args, **kwargs)