from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book
from django.core.paginator import Paginator
from .models import Purchase
from decimal import Decimal

# Create your views here.
categories = ["玄幻", "奇幻", "武侠", "仙侠", "都市", "现实", "军事", "历史", "游戏", "体育", "科幻", "诸天无限", "悬疑", "轻小说"]
def index(request):

    return render(request, "store/index.html", {'all_types': categories})

# def all(request):
#     books = Book.objects.all()
#     return render(request, "store/all_books.html", {'books': books})

def all(request):

    book_list = Book.objects.all()
    paginator = Paginator(book_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "store/all_books.html", {
        'page_obj': page_obj,
        'book_count': paginator.count,
        'all_types': categories,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, '用户名和密码不能为空，请填写完整。')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'欢迎回来，{username}！登录成功。')
            return redirect('index')
        else:
            messages.error(request, '用户名或密码错误，请重试。')
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

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'store/book_detail.html', {'book': book})

def buy_book(request, book_id):
    if not request.user.is_authenticated:
        messages.error(request, "请先登录后再购买！")
        return redirect('login')

    book = get_object_or_404(Book, id=book_id)
    profile = request.user.profile

    # ✅ 判断是否已购买过
    if Purchase.objects.filter(user=request.user, book=book).exists():
        messages.warning(request, f"你已经购买过《{book.title}》啦～不需要重复购买哦 💖")
        return redirect('book_detail', book_id=book.id)

    # 继续原来的购买逻辑
    if profile.balance >= book.price:
        profile.balance -= book.price
        profile.save()

        # 保存购买记录
        Purchase.objects.create(
            user=request.user,
            book=book,
            price_at_purchase=book.price
        )

        messages.success(request, f"成功购买《{book.title}》，已扣除 ￥{book.price} 元！")
    else:
        messages.error(request, "余额不足，无法购买该书籍。该给我爆金币了😘")

    return redirect('book_detail', book_id=book.id)

@login_required
def purchase_history(request):
    purchases = request.user.purchases.select_related('book').order_by('-purchase_time')
    return render(request, 'store/purchase_history.html', {'purchases': purchases})

@login_required
def add_balance(request):
    profile = request.user.profile
    profile.balance += Decimal('1000.00')
    profile.save()
    messages.success(request, "余额已增加1000元，快去买喜欢的书吧！🎉")
    return redirect('profile')
