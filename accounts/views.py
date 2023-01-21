from django.http import HttpResponse
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import GuestEmail
from .forms import LoginForm, RegisterForm, GuestForm
from store.models import Store


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)

        request.session['guest_email_id'] = new_guest_email.id

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/cart/checkout/")
    return redirect("/cart/checkout/")


User = get_user_model()


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if request.user.is_authenticated:
        return redirect('/')

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                qs = User.objects.get(username=username)
                if qs.user_type == "buyer":
                    return redirect("/products/")
                else:
                    return redirect("/")
        else:
            print("Error")
            context["error"] = "Username and Password do not match!"
    return render(request, "accounts/login.html", context)


# admin abc*1234


def register_page(request):
    form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    context = {
        "title": "Login",
        "content": "Login",
        "form": form
    }
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user_type = form.cleaned_data.get("user_type")
        new_user = User.objects.create_user(email, username, name, user_type, password)

        if user_type == "seller":
            request.session['username'] = username
            return redirect("/sell/")
        return redirect("/login/")
    return render(request, "accounts/register.html", context)


def edit_view(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            "title": "Edit Profile",
            "user": user,
        }

        if request.method == "POST":
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if email != "":
                user.eamil = email
                user.save()

                return redirect("/")
            if password1 != "":
                if password1 != password2:
                    context["error"] = "Password do not match"
                else:
                    user.set_password(password1)
                    user.save()

                    return redirect("/")
        return render(request, "accounts/edit.html", context)
    else:
        return redirect("/login/")


def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            "user": user
        }
        if user.user_type == "seller":
            store = Store.objects.get(owner=user)
            context["store"] = store
        return render(request, "accounts/profile.html", context)
    else:
        return redirect("/login/")
