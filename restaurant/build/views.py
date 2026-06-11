from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def index(request):
    return render(request, 'build/index.html', {
        "items": Item.objects.all()
    })

def cart(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(cart=cart)
    
    total = 0

    for cart_item in cart_items:
        total += cart_item.item.price * cart_item.quantity

    return render(request, 'build/cart.html', {
        "cart_items": cart_items,
        "total":total
    })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            Cart.objects.create(user=user)

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'build/register.html', {
        "form": form
    })

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'build/signin.html', {
        "form": form
    })

def logout_view(request):
    logout(request)
    return redirect('home')

def add_to_cart(request):
    if request.method == "POST":
        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        item_id = request.POST.get("item_id")
        item = get_object_or_404(Item, pk=item_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect("cart")

def remove_from_cart(request):
    if request.method == "POST":
        cart_item_id = request.POST.get("cart_item_id")

        cart_item = get_object_or_404(CartItem, id=cart_item_id)

        cart_item.delete()

    return redirect("cart")