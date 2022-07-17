from django.urls import path
from .views import index_view, commande_view, contact_view, detail_view, shop_view, cart_view


urlpatterns = [
    path('', index_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('detail/', detail_view, name='detail'),
    path('commande/', commande_view, name='commande'),
    path('boutique/', shop_view, name='boutique'),
    path('panier/', cart_view, name='panier'),
]