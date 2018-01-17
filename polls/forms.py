#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : algo_exe
@Time : 2018/1/12 下午4:53
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : forms.py
@desc :
"""
from django import forms


class ContactInfoForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)


if __name__ == '__main__':
    pass
