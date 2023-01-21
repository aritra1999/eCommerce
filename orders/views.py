from django.shortcuts import render


def store_view(request):
    user = request.user
    context = {

    }
    return render(request, "orders/store.html", context)
