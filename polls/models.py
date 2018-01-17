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
@File    : models.py
@desc    :
"""
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=512, help_text='description question')
    pub_date = models.DateTimeField('date published', help_text='question publish date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text='related to polls_question table')
    choice_text = models.CharField(max_length=512, help_text='question choice text description')
    votes = models.IntegerField(default=0, help_text='choice selected times')

    def __str__(self):
        return self.choice_text


if __name__ == '__main__':
    pass
