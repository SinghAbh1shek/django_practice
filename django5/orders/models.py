from django.db import models
from accounts.models import Customer
from products.models import VendorProduct


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_cart')
    is_paid = models.BooleanField(default=False)

    def has_product(self, product):
        return self.cart_items.filter(product=product).exists()

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(VendorProduct, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)

    def getTotalPrice(self):
        return self.quantity * self.product.vendor_selling_price

