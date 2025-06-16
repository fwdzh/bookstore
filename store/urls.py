from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all/', views.all, name = 'all'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/buy/', views.buy_book, name='buy_book'),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
    path('add_balance/', views.add_balance, name='add_balance'),
]