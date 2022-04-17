from django.db import models
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    

class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, related_name='produits')
    prix = models.FloatField(default=0)
    image = models.ImageField(upload_to='images')
    quantite = models.IntegerField(default=0)
    disponible = models.BooleanField()


class Client(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


class Commande(models.Model):
    date = models.DateTimeField(default=None)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.PROTECT, related_name='commandes')
    client = models.ForeignKey(Client, null=True, on_delete=models.PROTECT, related_name='commandes')

