from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # TODO 文献检索库的主界面
    ...


@login_required
def upload(request):
    # TODO 文献上传页面
    ...


@login_required
def statistics(request):
    # TODO 显示平台的文献统计数据，画个饼状图显示各个组的文献占比，显示各个人的文献占比等等
    ...
