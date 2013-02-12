#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    price = models.DecimalField( max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.title