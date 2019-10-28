from django.shortcuts import render, redirect

from orders.models import Order
from products.models import Product
from billing.models import BillingProfile
from .models import Cart
from addresses.forms import AddressForm
from addresses.models import Address
from accounts.forms import LoginForm, GuestForm
from django.contrib.auth import get_user_model

User = get_user_model()
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product_list = Product.objects.all()
    context = {
        "cart": cart_obj,
        "product_list":product_list,
    }
    return render(request, "carts/home.html", context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.products.add(product_obj)  # cart_obj.products.add(product_Aid)
            added = True
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")



def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count == 0:
        return redirect("cart:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    # shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    product_list = Product.objects.all()

    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        # if shipping_address_id:
        #     order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
        #     del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        # if billing_address_id or shipping_address_id:
        #     order_obj.save()
        if billing_address_id:
            order_obj.save()

    if request.method == "POST":
        "Some check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("cart:success")

    if request.user.is_authenticated:
        old_billing_profile = BillingProfile.objects.get(user=request.user)
        old_addresses = Address.objects.filter(billing_profile=old_billing_profile)
    else:
        old_addresses = ""


    # cart_qs = Cart.objects.get(user=request.user)
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    context = {
        "product_list":product_list,
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "old_addresses":old_addresses,
        "cart":cart_obj,

    }
    return render(request, "carts/checkout.html", context)

def checkout_done_view(request):
    obj = Product.objects.all()
    cart = Cart.objects.all()
    product_list = Product.objects.all()
    context ={
        "title": "eComm | Success",
        "obj": obj,
        "product_list": product_list,
        # "cart": cart,
    }
    return render(request, "carts/checkout-done.html", context)
