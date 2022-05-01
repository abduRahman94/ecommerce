from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'shop/index.html')


def contact_view(request):
    return render(request, 'shop/contact.html')


def commande_view(request):
    return render(request, 'shop/checkout.html')


def detail_view(request):
    return render(request, 'shop/detail.html')


def shop_view(request):
    return render(request, 'shop/shop.html')


def cart_view(request):
    return render(request, 'shop/cart.html')
