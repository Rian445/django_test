from django.shortcuts import render, redirect
from .models import Product, CartItem, PurchaseHistory


def shop_home(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.all()
    purchase_history = PurchaseHistory.objects.all()[
        :10]

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)
            CartItem.objects.create(product=product)
            return redirect('shop:home')

    total = sum(item.product.price for item in cart_items)

    return render(request, 'shop/home.html', {
        'products': products,
        'cart_items': cart_items,
        'total': total,
        'purchase_history': purchase_history
    })


def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price for item in cart_items)

    if request.method == 'POST':
        if cart_items:
            # Create purchase history
            items_list = [item.product.name for item in cart_items]
            items_purchased = ', '.join(items_list)

            PurchaseHistory.objects.create(
                total_amount=total,
                items_purchased=items_purchased
            )

            # Clear cart
            cart_items.delete()
            return redirect('shop:thank_you')

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'empty': len(cart_items) == 0
    })


def thank_you(request):
    return render(request, 'shop/thank_you.html')
