import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()
from products.models import *

from django.db.models import Avg, Min, Max, Count, Sum, Q, Subquery, OuterRef

# product = VendorProduct.objects.aggregate(price = Max('vendor_selling_price'))
# print(product)

# shopkeepers = Shopkeeper.objects.annotate(count = Count('products', filter=Q(products__created_at__year__gte = 2025)), avg = Avg('products__vendor_selling_price'), total_price = Sum('products__vendor_selling_price'))
# shopkeepers = Shopkeeper.objects.annotate(count = Count('products', filter=Q(products__vendor_selling_price__gte = 1000)), total_price = Sum('products__vendor_selling_price')).filter(count__gte = 1)

# for shopkeeper in shopkeepers:
#     print(f"{shopkeeper.shop_name} num of product {shopkeeper.count} and total price: {shopkeeper.total_price}")
# print(shopkeepers)


# print(Category.objects.count())

# categories = Category.objects.filter(parent__isnull = True).prefetch_related('cat_child')
# for cat in categories:
#     child1 = cat.cat_child.first()
#     print(child1.cat_child.exists())
#     print(child1.cat_child.first().cat_child.exists())

# for cat in categories:
#     print(f"Parent: {cat.category_name}")
#     for child in cat.cat_child.all():
#         print("  └──", child.category_name)

# def get_children(category, level=0):
#     print("  " * level + f"- {category.category_name}")
#     for child in category.cat_child.all():
#         get_children(child, level + 1)

# print(Category.objects.count())
# parents = Category.objects.filter(parent__isnull=True).prefetch_related('cat_child__cat_child')

# for parent in parents:
#     get_children(parent)



vendor = VendorProduct.objects.filter(
    shopkeeper = OuterRef('id')
).order_by('-created_at').values('product__title')[:1]
# shopkeepers = Shopkeeper.objects.all()
shopkeepers = Shopkeeper.objects.annotate(vendor_product = Subquery(vendor))

for shopkeeper in shopkeepers:
    # print(shopkeeper.shop_name)
    print(shopkeeper.vendor_product)