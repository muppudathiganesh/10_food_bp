from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem, Order
from restaurant.models import MenuItem

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum([i.subtotal() for i in items])
    return render(request, 'orders/cart.html', {'items': items, 'total': total})

def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum([i.subtotal() for i in items])
    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=total)
        order.items.set(items)
        items.delete()
        return redirect('cart')
    return render(request, 'orders/checkout.html', {'items': items, 'total': total})
