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
from snippets import views

app_name = 'snippets'
urlpatterns = [
    path('', views.snippet_list, name='index'),
    path('<int:pk>/', views.snippet_detail, name='detail'),
]

if __name__ == '__main__':
    pass
