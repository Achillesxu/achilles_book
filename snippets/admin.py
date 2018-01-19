#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : achilles_book
@Time    : 2017/11/6 22:02
@Author  : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site    :
@File    : admin.py
@desc    :
"""
from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Snippet information', {'fields': ['title', 'code', 'linenos', 'language', 'style']}),
    ]


# Register your models here.
admin.site.register(Snippet, SnippetAdmin)
