from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], group_name=request.POST['group_name'])
        new_user.save()
        login(request, new_user)
        return render(reverse('index'))
    else:
        return HttpResponseRedirect(request, 'user/register.html')


def login(request):
    # TODO 登录界面
    ...


def index(request):
    # TODO 显示用户自己的相关信息
    ...
