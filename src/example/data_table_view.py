#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bob.data_table import DataTableMixin, DataTableColumn
from example.models import Book
from example.views import BaseView


class DataTableView(BaseView, DataTableMixin):
    template_name = "data_table.html"
    sort_variable_name = 'sort'
    rows_per_page = 5
    export_variable_name = 'export'

    _ = DataTableColumn
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
