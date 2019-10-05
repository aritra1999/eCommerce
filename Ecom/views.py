from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Home",
        "content": "Hello World",
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About",
        "content": "About Us",
    }
    return render(request, "home_page.html", context)




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