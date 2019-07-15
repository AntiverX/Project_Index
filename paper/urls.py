#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @ProjectName  : Project_Index
# @FileName     : urls.py
# @Description  : 
# @CreateTime   : 2019/7/12 17:10
# @Author       : Men
from django.conf.urls import url

from . import views

urlpatterns = [
    url('index', views.index),
    # url(r'show', views.show),
    url('create', views.CreateView.as_view(), name='create'),
    url('<int:id>', views.DetailView.as_view(), name='detail'),
    url('dashboard', views.statistics),
]
