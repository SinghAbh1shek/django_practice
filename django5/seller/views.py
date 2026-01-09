from django.shortcuts import render, redirect
from products.models import VendorProduct, Category
from orders.models import OrderItems
from django.db.models import Sum, F
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
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


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Category, Product, VendorProduct

@login_required(login_url='login')
def seller_add_product(request):
    shopkeeper = request.user.shopkeeper

    categories = Category.objects.filter(cat_child__isnull=True)

    selected_category_id = request.GET.get('category')

    if selected_category_id:
        product_lists = Product.objects.filter(
            category_id=selected_category_id
        )
    else:
        product_lists = Product.objects.none()

    if request.method == "POST":
        product_id = request.POST.get('product')
        price = request.POST.get('price')
        is_active = request.POST.get('is_active') == 'on'


        if product_id and price:
            VendorProduct.objects.get_or_create(
                shopkeeper=shopkeeper,
                product_id=product_id,
                defaults={
                    'vendor_selling_price': price,
                    'is_active': is_active
                }
            )

        return redirect('list_product')

    context = {
        'categories': categories,
        'product_lists': product_lists,
        'selected_category_id': selected_category_id
    }

    return render(request, 'add_product.html', context)


@login_required(login_url='login')
def list_product(request):
    shopkeeper = request.user.shopkeeper
    products = VendorProduct.objects.filter(shopkeeper = shopkeeper)
    print(products)
    context = {
        'products': products
    }
    return render(request, 'list_product.html', context)
