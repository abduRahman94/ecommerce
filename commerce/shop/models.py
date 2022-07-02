from django.db import models


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200, null=True)


class SousCategorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, related_name='sous_categories')


class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200, null=True)
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, null=True, related_name='produits')
    prix = models.FloatField(default=0)
    image = models.ImageField(upload_to='images')
    quantite = models.IntegerField(default=0)
    disponible = models.BooleanField()


class Client(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


class Commande(models.Model):
    date = models.DateTimeField(default=None)
    reference_commande = models.CharField(max_length=200)
    client_id = models.ForeignKey(Client, null=True, on_delete=models.PROTECT, related_name='commandes')


class DetailCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True, related_name='details_commandes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True, related_name='details_commandes')
    quantite = models.IntegerField(default=0)
    prix = models.FloatField(default=0)


class Panier(models.Model):

    liste_produits = []

    # add a product to the cart
    def add_product(self, produit, quantite):
        self.liste_produits.append({'produit': produit, 'quantite': quantite})
        return self.liste_produits

    # get list of products in the cart
    def get_list_products(self):
        return self.liste_produits

    # remove a product from the cart
    def remove_product(self, produit):
        for produit_panier in self.liste_produits:
            if produit_panier['produit'] == produit:
                self.liste_produits.remove(produit_panier)
                return self.liste_produits

    # get the total price of the cart
    def get_total_price(self):
        total_price = 0
        for produit_panier in self.liste_produits:
            total_price += produit_panier['produit'].prix * produit_panier['quantite']
        return total_price

    # get the total quantity of the cart
    def get_total_quantity(self):
        total_quantity = 0
        for produit_panier in self.liste_produits:
            total_quantity += produit_panier['quantite']
        return total_quantity
