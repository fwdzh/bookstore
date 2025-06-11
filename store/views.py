from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book

# Create your views here.

def index(request):
    all_types = ['玄幻', '奇幻', '武侠', '仙侠', '都市', '现实', '军事', '历史', '游戏', '体育', '科幻', '诸天无限', '悬疑', '轻小说']

    return render(request, "store/index.html", {'all_types': all_types})

def all(request):
    books = Book.objects.all()
    return render(request, "store/all_books.html", {'books': books})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'登录成功{username}!!!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "用户名已存在，请更换用户名后重试！")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "注册成功，请登录！")
        return redirect('login')
    return render(request, 'store/register.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'store/profile.html', {'user': user})
