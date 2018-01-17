#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : algo_exe
@Time : 2018/1/3 下午1:48
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : urls.py
@desc :
"""
from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.PollIndexView.as_view(), name='index'),
    path('<int:pk>/', views.PollDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.PollResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('start_index/', views.start_index, name='start_index'),
    path('about_page/', views.AboutPage.as_view(), name='about_page'),
]


if __name__ == '__main__':
    pass
