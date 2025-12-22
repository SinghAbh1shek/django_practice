from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import *
from django.db.models import Count

def index(request):
    categories = Category.objects.annotate(
        product_count=Count('cat_child__products', distinct=True)).filter(product_count__gt = 0).order_by("-id")[:10]
    
    for category in categories:
        image = (
            ProductImage.objects
            .filter(product__category__parent=category)
            .select_related('product')
            .first()
        )
        category.display_image = image.image.url if image else None
    

    new_arrivals = ( VendorProduct.objects.filter(product__images__isnull=False)
    .order_by('-created_at').distinct()[:5]
    )

    trending = (VendorProduct.objects.filter(product__images__isnull=False)
    .order_by('-product__trending_score').distinct()[:5]
    )

    top_rated = (VendorProduct.objects.filter(product__images__isnull=False)
    .order_by('-product__product_rating').distinct()[:5]
    )

    new_products = (VendorProduct.objects.filter(product__images__isnull = False)
                   .order_by('-created_at').distinct()[:12])


    context = {
        'categories': categories,
        'new_arrivals': new_arrivals,
        'trending': trending,
        'top_rated': top_rated,
        'new_products': new_products,
        }

    return render(request, 'home.html', context)
