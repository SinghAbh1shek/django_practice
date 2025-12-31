from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Cart, CartItems
from accounts.models import Customer
from products.models import VendorProduct
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def get_cart(request):
    cart = None
    try:    
        cart = Cart.objects.get(customer = request.user.customer, is_paid = False)
    except Exception as e:
        print("Something Wrong")
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

def remove_item_from_cart(request):
    try:
        product_id = request.GET.get("product_id")
        product = VendorProduct.objects.get(id = product_id)
        cart = Cart.objects.get(customer = request.user.customer, is_paid=False)
        cart_items = CartItems.objects.filter(cart = cart, product = product)
        if cart_items.exists():
            cart_items.delete()
            cart_items.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

    except Exception as e:
        print('Something goes wrong')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def empty_cart(request):
    try:
        cart = Cart.objects.get(customer = request.user.customer, is_paid=False)
        cart.clear_cart()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        print('Something goes wrong')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))