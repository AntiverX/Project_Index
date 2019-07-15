from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], group_name=request.POST['group_name'])
        new_user.save()
        login(request, new_user)
        return render(reverse('index'))
    else:
        return render(request, 'user/register.html')


def auth(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            context['error'] = "用户名或密码错误"
            return render(request, "error.html", context=context)
    else:
        return render(request, 'user/login.html')


def index(request):
    # 显示用户的相关信息
    return render(request, 'user/index.html')
