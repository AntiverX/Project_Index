from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], group_name=request.POST['group_name'])
        new_user.save()
        login(request, new_user)
        return render(reverse('index'))
    else:
        return HttpResponseRedirect(request, 'user/register.html')


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
    # TODO 显示用户自己的相关信息
    ...
