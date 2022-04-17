from django.contrib import admin
from .models import Categorie, Produit, Commande, Client

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Client)
