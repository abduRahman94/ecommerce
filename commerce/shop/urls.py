from django.urls import path
from .views import index_view, commande_view, contact_view, detail_view, shop_view, cart_view


urlpatterns = [
    path('index/', index_view),
    path('contact/', contact_view),
    path('detail/', detail_view),
    path('commande/', commande_view),
    path('boutique/', shop_view),
    path('panier/', cart_view),
]