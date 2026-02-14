from django.contrib import admin
from .models import Categorie, Produit, Commande
from django.contrib import admin
from .models import Categorie, Produit, Commande

# Configuration de l'interface
admin.site.site_header = "Sen_charcuterie"      # Le texte dans la barre bleue en haut
admin.site.site_title = "Sen_charcuterie Admin" # Le texte dans l'onglet du navigateur
admin.site.index_title = "Gestion de la boutique" # Le titre sur la page d'accueil de l'admin

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_add') 

class AdminProduit(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout', 'prix', 'categorie')
    search_fields = ('nom', )  # Permet de rechercher par nom
    list_editable = ('prix', 'categorie')  # Permet d'éditer directement le prix et la catégorie depuis la liste

class AdminCommande(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'region', 'commune', 'total','date_commande')

admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Commande, AdminCommande)