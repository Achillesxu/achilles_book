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
from django.contrib.auth.models import User
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html')
#
#     class Meta:
#         model = Snippet
#         fields = ('url', 'id', 'highlight', 'owner',
#                   'title', 'code', 'linenos', 'language', 'style')
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'snippets')


if __name__ == '__main__':
    pass
