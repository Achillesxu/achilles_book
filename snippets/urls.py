#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : achilles_book
@Time : 2018/1/19 上午10:18
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : urls.py
@desc :
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.schemas import get_schema_view
from snippets import views

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

schema_view = get_schema_view(title='Pastebin API')


app_name = 'snippets'
urlpatterns = [
    # path('', views.snippet_list, name='index'),
    # path('<int:pk>/', views.snippet_detail, name='detail'),
    # path('', views.api_root, name='index'),
    # path('snippet-list/', views.SnippetList.as_view(), name='snippet-list'),
    # path('snippet-list/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    # path('user-list/', views.UserList.as_view(), name='user-list'),
    # path('user-list/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('', views.api_root, name='index'),
    path('snippet-list/', snippet_list, name='snippet-list'),
    path('snippet-list/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('user-list/', user_list, name='user-list'),
    path('user-list/<int:pk>/', user_detail, name='user-detail'),
    path('<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('schema/', schema_view, name='snippet-schema')
]
urlpatterns = format_suffix_patterns(urlpatterns)

if __name__ == '__main__':
    pass
