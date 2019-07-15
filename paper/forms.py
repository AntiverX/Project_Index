#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @ProjectName  : Project_Index
# @FileName     : forms.py
# @Description  : 
# @CreateTime   : 2019/7/15 9:37
# @Author       : Men
from django import forms
from django.forms import ModelForm

from paper.models import JournalPaper


class BasePaperForm(forms.Form):
    title = forms.CharField(label="标题", max_length=512)
    sub_title = forms.CharField(label="副标题", max_length=512)
    author = forms.CharField(label="作者", max_length=256)
    keywords = forms.CharField(label="关键词", max_length=512)


class JournalPaperForm(ModelForm):
    class Meta:
        model = JournalPaper
        fields = [
            'title', 'sub_title',
            'author',
            'keywords',
            'journal', 'volume', 'pages'
        ]


class ConferencePaperForm(BasePaperForm):
    conference = forms.CharField(label="会议", max_length=512)


class ThesisPaperForm(BasePaperForm):
    university = forms.CharField(label="学校", max_length=128)
    degree = forms.CharField(label="学位", max_length=32)
    mentor = forms.CharField(label="导师", max_length=64)
