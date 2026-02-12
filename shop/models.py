from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    date_add = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_add'] # Added '-' to show newest first by default
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE)
    # Modification ici : on utilise ImageField et on définit le dossier de stockage
    image = models.ImageField(upload_to='produits/%Y/%m/%d/', blank=True, null=True) 
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom
