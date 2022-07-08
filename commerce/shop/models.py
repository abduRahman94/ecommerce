from django.db import models
import uuid


STATUT_COMMANDE = (
    ('0', 'En attente'),
    ('1', 'Payée'),
    ('2', 'Livrée'),
    ('3', 'Annulée'),
)

MODE_PAIEMENT = (
    ('0', 'Espèces'),
    ('1', 'Orange Money'),
    ('2', 'Wave'),
)


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
    reference_commande = models.UUIDField(default=uuid.uuid4, editable=False)
    client_id = models.ForeignKey(Client, null=True, on_delete=models.PROTECT, related_name='commandes')
    statut = models.CharField(max_length=1, choices=STATUT_COMMANDE, default='0')
    mode_paiement = models.CharField(max_length=1, choices=MODE_PAIEMENT, default='0')

    # update mode_paiement
    def update_mode_paiement(self, mode_paiement):
        self.mode_paiement = mode_paiement
        self.save()

    # update statut
    def update_statut(self, statut):
        self.statut = statut
        self.save()

    # process commande
    def traiter_commande(self, liste_produits):
        for item in liste_produits:
            ProduitsCommande.objects.create(commande_id=self.reference_commande,
                                            produit=item.produit.id,
                                            quantite=item.produit.quantite,
                                            prix=item.produit.prix,
                                            total=item.produit.prix * item.produit.quantite)

    # annuler commande
    @staticmethod
    def annuler_commande(self, reference_commande):
        ProduitsCommande.objects.filter(reference_commande=reference_commande).delete()


class ProduitsCommande(models.Model):
    commande_id = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True, related_name='produits_commande')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    quantite = models.IntegerField(default=0)
    prix = models.FloatField(default=0)
    total = models.FloatField(default=0)


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
