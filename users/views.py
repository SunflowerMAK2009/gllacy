from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import UserRegestrationForm, UserProfileForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from catalog.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegestrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_url")
    else:
        form = UserRegestrationForm()
        return render(request, "users/register.html", context={"form": form})

@login_required
def edit_profile(request):
    user = request.user
    profile_form = UserProfileForm(instance=user)
    password_form = PasswordChangeForm(user)
    if request.method == "POST":
        if "profile_submit" in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Ваш профиль был успешно обновлен!")
                return redirect("edit_profile")
            else:
                messages.error(request, "Произошла ошибка при изменении профиля, проверьте введенные данные!")
        elif "password_submit" in request.POST:
            password_form = PasswordChangeForm(user,request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Ваш пароль был успешно изменен!")
                return redirect("edit_profile")
            else:
                messages.error(request, "Произошла ошибка при изменении пароля, проверьте введенные данные!")
    return render(request, "users/edit_profile.html", context={"profile_form": profile_form, "password_form": password_form})

@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cartitem, cartitem_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not cartitem_created:
            cartitem.number += 1
            cartitem.save()
        items = cart.items.all()
        for item in items:
            item.total_price = item.get_total_price()
        total_count = items.count()
        cart_html = render_to_string('cart.html', {"cart_items": items, "cart_total_sum": cart.get_total_sum()})
        return JsonResponse({
            'cart_html': cart_html,
            'total_count': total_count,
            'success': True
        })
    else:
        return JsonResponse({
            'success': False,
            'error': 'Only post allowed'
        })

@login_required
def delete_from_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cartitem = cart.items.filter(product=product).first()
        if cartitem:
            cartitem.delete()
        items = cart.items.all()
        for item in items:
            item.total_price = item.get_total_price()
        total_count = items.count()
        cart_html = render_to_string('cart.html', {"cart_items": items, "cart_total_sum": cart.get_total_sum()})
        return JsonResponse({
            'cart_html': cart_html,
            'total_count': total_count,
            'success': True
        })
    else:
        return JsonResponse({
            'success': False,
            'error': 'Only post allowed'
        })













