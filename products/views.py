from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

from .models import Product
from store.models import Store
from .forms import AddProductFrom
from carts.models import Cart
from orders.models import Placed


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class ProductListView(ListView):
    queryset = Product.objects.all().order_by('timestamp')
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()




def product_detail_view(request, slug=None, *args, **kwargs):
    instance = Product.objects.get(slug=slug)
    if instance is None:
        raise Http404("Product doesn't exist")

    owner = instance.seller
    store = Store.objects.get(owner=owner)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product_list = Product.objects.all()

    context = {
        "object": instance,
        "store": store,
        "cart": cart_obj,
        "product_list": product_list,
    }

    return render(request, "products/detail.html", context)

User = get_user_model()


def addproduct(request):
    if request.user.is_authenticated:
        user_type = request.user.user_type
        if user_type == 'seller':
            form = AddProductFrom(request.POST or None, request.FILES or None)
            context = {
                "form": form,
                "title": "Add Product",
            }

            username = request.user.username
            username_instance = User.objects.get(username=username)
            store_name_instance = Store.objects.get(owner=username_instance)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.seller = username_instance
                instance.store_name = store_name_instance
                instance.save()
                return redirect("/")
            else:
                print("Debug: ", form.errors)
            return render(request, "products/addproduct.html", context)
        return redirect("/products/")
    return redirect("/products/")

def deleteproduct(request, slug):
    if request.user.is_authenticated:
        product = Product.objects.get(slug=slug)
        if product.seller == request.user:
            if request.method == "POST":
                product_id = request._post.get('product_id')
                Product.objects.filter(id=product_id).delete()
                return redirect("/")
            context = {
                "product": product,
                "title": "Delete Product?",
            }
            return render(request, "products/deleteproduct.html", context)
        else:
            return redirect("")
    else:
        return redirect("/login/")

def placed_view(request):
    if request.user.is_authenticated:
        price = 0
        orders = Placed.objects.filter(buyer_email=request.user.email)
        for order in orders:
            price = price + order.product.price
        total = {
            "price":price,
        }
        context = {
            "title":"Previous Orders",
            "orders":orders,
            "total": total,
        }
        return render(request, "products/placed.html", context)
    return redirect("/products/")