from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm
from products.models import Product

def home_page(request):
    product_list = Product.objects.all()
    context = {
        "title": "Home",
        "content": "Hello World",
        "product_list": product_list,
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About",
        "content": "About Us",
    }
    return render(request, "about/about.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us",
        "content": "Contact Us",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/contact.html", context)