#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : algo_exe
@Time : 2018/1/4 下午2:32
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : jinja2.py
@desc :
"""
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.add_extension('jinja2.ext.i18n')
    return env


if __name__ == '__main__':
    pass
