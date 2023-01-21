from django.conf.urls import url

from .views import (ProductListView,
                    # ProductDetailView,
                    # ProductFeaturedDetailView,
                    # ProductFeaturedListView,
                    ProductDetailSlugView,
                    product_detail_view,
                    )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    # url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', product_detail_view, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(), name='download'),
]

