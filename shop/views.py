from django.shortcuts import render, redirect
from django.db.models import Count, Q
from .models import Product, CartItem, PurchaseHistory
from collections import defaultdict
import json

def shop_home(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.all()
    purchase_history = PurchaseHistory.objects.all()[:10]

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)
            CartItem.objects.create(product=product)
            return redirect('shop:home')

    total = sum(item.product.price for item in cart_items)
    
    # statistics for pie chart
    all_purchases = PurchaseHistory.objects.all()
    product_sales_count = defaultdict(int)
    
    # how many time 
    for purchase in all_purchases:
        items_list = [item.strip() for item in purchase.items_purchased.split(',')]
        for item in items_list:
            product_sales_count[item] += 1
    
    # Sort products  (most sold first)
    sorted_sales = sorted(product_sales_count.items(), key=lambda x: x[1], reverse=True)
    total_sales = sum(product_sales_count.values())
    
    # Calculate percentages for each product
    product_data = []
    for product_name, count in sorted_sales[:10]:  # Top 10 products
        percentage = round((count / total_sales * 100), 1) if total_sales > 0 else 0
        product_data.append({
            'name': product_name,
            'count': count,
            'percentage': percentage
        })
    
    # Prepare chart data
    chart_data = {
        'labels': [item['name'] for item in product_data],
        'data': [item['count'] for item in product_data],
        'percentages': [item['percentage'] for item in product_data],
        'total_sales': total_sales,
        'product_stats': product_data
    }
    
    context = {
        'products': products,
        'cart_items': cart_items,
        'total': total,
        'purchase_history': purchase_history,
        'chart_data': chart_data,
        'has_sales_data': len(sorted_sales) > 0
    }
    
    return render(request, 'shop/home.html', context)

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
