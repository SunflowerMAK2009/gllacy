from .models import Cart

def cart_context(request):
    if not request.user.is_authenticated:
        return {}
    else:
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        total_sum = cart.get_total_sum()
        for item in items:
            item.total_price = item.get_total_price()
        return {"cart_items": items, "cart_total_sum": total_sum}
