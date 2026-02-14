from django.contrib import admin
from .models import Categorie, Produit, Commande

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_add') 

class AdminProduit(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout', 'prix', 'categorie')

class AdminCommande(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'region', 'commune', 'total','date_commande')

admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Commande, AdminCommande)