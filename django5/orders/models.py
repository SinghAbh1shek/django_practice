from django.db import models
from accounts.models import Customer
from products.models import VendorProduct
from django.db.models import Sum, F
from utils.utility.models import BaseModel


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_cart')
    is_paid = models.BooleanField(default=False)

    def has_product(self, product):
        return self.cart_items.filter(product=product).exists()
    
    def getCartTotal(self):
        total = self.cart_items.aggregate(
            total = Sum(F('product__vendor_selling_price') * F('quantity'))
        )['total']
        return total or 0
    
    def clear_cart(self):
        self.cart_items.all().delete()

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(VendorProduct, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)

    def getTotalPrice(self):
        return self.quantity * self.product.vendor_selling_price
    
class Wishlist(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlists')

    def has_product(self, product):
        return self.items.filter(product = product).exists()
    
    def add_product(self, product):
        self.items.get_or_create(product = product)
    
    def remove_product(self, product):
        self.items.filter(product = product).delete()

class WishlistItems(BaseModel):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(VendorProduct, on_delete=models.CASCADE)

