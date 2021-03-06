from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login_page, register_page, guest_register_view, edit_view, profile_view
from .views import home_page, contact_page, about_page
from addresses.views import (
    checkout_address_create_view,
)
from products.views import addproduct, placed_view, deleteproduct
# from carts.views import cart_home
from store.views import store_registration_view


urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^about/$', about_page, name='about'),
    url(r'^login/$', login_page, name='buyerlogin'),
    url(r'^edit/$', edit_view, name='edit'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^addproduct', addproduct, name='addproduct'),
    url(r'^sell/$', store_registration_view, name='sellerregistration'),
    url(r'^register/$', register_page, name='buyerregistration'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^admin/', admin.site.urls),
    url(r'^products/',include(('products.urls', 'products'), namespace='products')),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
    url(r'^cart/', include(('carts.urls', 'carts') , namespace='cart')),
    url(r'^placed/', placed_view, name="placed"),
    url(r'^delete/(?P<slug>[\w-]+)/$', deleteproduct, name="delete"),
    # url(r'^carts/', include(('carts.urls', 'carts'), namespace='carts')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)