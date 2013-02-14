#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bob.menu import MenuItem
from bob.data_table import DataTableMixin, DataTableColumn
from django.views.generic import TemplateView
from example.models import Book
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


class DataTableExample(DataTableColumn):
    def __init__(self, header_name, sort_expression=None, export=None,
                 **kwargs):
        super(DataTableExample, self).__init__(header_name, **kwargs)
        self.sort_expression = sort_expression
        self.export = export


class DataTableView(BaseView, DataTableMixin):
    template_name = "data_table.html"
    sort_variable_name = 'sort'
    rows_per_page = 5
    export_variable_name = 'export'

    _ = DataTableExample
    columns = [
        _(
            'Dropdown',
            selectable=True,
            bob_tag=True,
        ),
        _(
            'Title',
            field='title',
            sort_expression='title',
            bob_tag=True,
            export=True,
        ),
        _(
            'Publication Date',
            field='pub_date',
            sort_expression='pub_date',
            bob_tag=True,
            export=True,
        ),
        _(
            'Price',
            field='price',
            sort_expression='price',
            bob_tag=True,
            export=True,
        ),
    ]

    def get_context_data(self, *args, **kwargs):
        ret = super(DataTableView, self).get_context_data(*args, **kwargs)
        ret.update(
            super(DataTableView, self).get_context_data_paginator(
                *args,
                **kwargs
            )
        )
        ret.update({
            'sort_variable_name': self.sort_variable_name,
            'url_query': self.request.GET,
            'sort': self.sort,
            'columns': self.columns,
        })
        return ret

    def get_csv_data(self, queryset):
        header = super(DataTableView, self).get_csv_header()
        data = []
        data.append(header)
        for book in queryset:
            row = []
            for item in self.columns:
                field = item.field
                if field:
                    cell = self.get_cell(book, field, Book)
                    row.append(unicode(cell))
            data.append(row)
        return data

    def get_query(self):
        books = Book.objects.all()
        self.data_table_query(books)

    def get(self, *args, **kwargs):
        self.get_query()
        if self.export_requested():
            return self.response
        return super(DataTableView, self).get(*args, **kwargs)

class HomeView(BaseView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        return  super(HomeView, self).get_context_data(*args, **kwargs)
