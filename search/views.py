from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
from django.db.models import Q

class SearchProductView1(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query  = request.GET.get('q', None)
        if query is not None:
            query_list = query.split(" ")
            result = list(Product.objects.none())
            for que in query_list:
                result.append(Product.objects.search(que))
            return result
        return Product.objects.none()

def SearchProductView(request):
    context = {
        "title": "Search",
    }
    if request.method == "GET":
        query = request.GET.get('q', None)
        context[query] = query
        if query is not None:
            query_list = query.split(" ")
            results = []
            for que in query_list:
                ins = Product.objects.filter((Q(title__icontains=que) |
                                               Q(color__icontains=que) |
                                               Q(category__icontains=que) |
                                               Q(price__icontains=que) |
                                               Q(tag__title__icontains=que)
                                               ))
                results.append(ins)

            context['query'] = query
            object_list = Product.objects.none()
            print(object_list)
            test = Product.objects.filter(color='red')
            for result in results:
                for product in result:
                    object_list |= Product.objects.filter(pk=product.pk)
            context['object_list'] = object_list
    return render(request, "search/view.html", context)