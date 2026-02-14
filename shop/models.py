from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    date_add = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_add']
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produits/%Y/%m/%d/', blank=True, null=True) 
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom

class Commande(models.Model):
    items = models.TextField() # Stocke le JSON du panier
    total = models.CharField(max_length=200)
    
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    adresse = models.TextField()
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom