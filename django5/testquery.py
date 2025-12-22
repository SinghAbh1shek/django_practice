import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()
from products.models import *

from django.db.models import Avg, Min, Max, Count, Sum, Q

# product = VendorProduct.objects.aggregate(price = Max('vendor_selling_price'))
# print(product)

# shopkeepers = Shopkeeper.objects.annotate(count = Count('products', filter=Q(products__created_at__year__gte = 2025)), avg = Avg('products__vendor_selling_price'), total_price = Sum('products__vendor_selling_price'))
shopkeepers = Shopkeeper.objects.annotate(count = Count('products', filter=Q(products__vendor_selling_price__gte = 1000)), total_price = Sum('products__vendor_selling_price')).filter(count__gte = 1)

for shopkeeper in shopkeepers:
    print(f"{shopkeeper.shop_name} num of product {shopkeeper.count} and total price: {shopkeeper.total_price}")
# print(shopkeepers)
