#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : achilles_book
@Time : 2018/1/19 上午9:54
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : serializers.py
@desc :
"""
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


if __name__ == '__main__':
    pass
