from django.contrib import admin
from .models import Categorie, Produit

class AdminCategorie(admin.ModelAdmin):
    # Ajout du signe "=" ici
    list_display = ('name', 'date_add') 

class AdminProduit(admin.ModelAdmin):
    # Ajout du signe "=" ici
    list_display = ('nom', 'date_ajout', 'prix', 'categorie')

admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)