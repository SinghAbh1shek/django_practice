from django.shortcuts import render
from products.models import VendorProduct
from orders.models import OrderItems
from django.db.models import Sum, Count, F
def home(request):

    shopkeeper = request.user.shopkeeper

    total_product = VendorProduct.objects.filter(
        shopkeeper = shopkeeper
    ).count()

    active_product = VendorProduct.objects.filter(
        shopkeeper = shopkeeper, is_active = True
    ).count()

    order_items = OrderItems.objects.filter(
        product__shopkeeper = shopkeeper,
        order__cart__is_paid = True
    )

    total_orders = order_items.values('order').distinct().count()

    total_revenue = order_items.aggregate(
        total = Sum(F('price') * F('quantity'))
    )['total'] or 0

    recent_orders = order_items.select_related(
        'order', 'product'
    ).order_by('-created_at')[:10]


    context = {
        'total_product': total_product,
        'active_product': active_product,
        'total_orders': total_orders,
        'total_revenue':total_revenue,
        'recent_orders': recent_orders
    }

    return render(request, 'seller_home.html', context)


def seller_add_product(request):
    return render(request, 'add_product.html')