from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cart, CartItems
from accounts.models import Customer
from products.models import VendorProduct

def get_cart(request):
    return render(request, 'cart.html')

def add_to_cart(request):
    try:
        user = request.user.id
        product = request.GET.get('product_id')
        customer = Customer.objects.get(user  = user)
        product = VendorProduct.objects.get(id = product)
        cart, _ = Cart.objects.get_or_create(customer = customer, is_paid = False)
        cart_item, _ = CartItems.objects.get_or_create(cart = cart, product = product)
        cart_item.quantity += 1
        cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print('Something is wrong')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def remove_to_cart(request):
    try:
        user = request.user.id
        customer = Customer.objects.get(user = user)
        product_id = request.GET.get('product_id')
        product = VendorProduct.objects.get(id = product_id)
        cart = Cart.objects.get(customer = customer, is_paid = False)
        cart_item = CartItems.objects.filter(cart = cart, product=product)
        if cart_item.exists():
            cart_item = cart_item[0]
            cart_item.quantity -= 1

            if cart_item.quantity <=0:
                cart_item.delete()
            else:
                cart_item.save()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        print(e)
        print('Something is wrong')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

