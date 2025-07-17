
from django.shortcuts import render, redirect
from .models import Product, CartItem


def shop_home(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.all()

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
        'total': total
    })


def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price for item in cart_items)

    pathao_pay_link = "https://pathaopay.me/@aornob445"

    if request.method == 'POST':

        cart_items.delete()
        return redirect(pathao_pay_link)

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'empty': False
    })
