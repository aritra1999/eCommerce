from django.shortcuts import render, redirect
from .forms import StoreRegistrationForm
from .models import Store
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, UserManager

User = get_user_model()


def store_registration_view(request):
    form = StoreRegistrationForm(request.POST or None)
    temp = request.session['username']
    context = {
        "form": form,
        "title": "Add Store",
        "temp": temp,
    }
    # owner = request.user.username
    owner = request.session['username']
    owner_instance = User.objects.get(username=owner)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = owner_instance
        instance.save()
        return redirect("/login/")
    else:
        print(form.errors)
    return render(request, "store/store_registration.html", context)
