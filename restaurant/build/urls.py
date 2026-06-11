from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('cart', views.cart, name="cart"),
    path('register', views.register, name="register"),
    path('login', views.signin, name="signin"),
    path('logout', views.logout_view, name="logout_view"),
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart', views.remove_from_cart, name="remove_from_cart")
]