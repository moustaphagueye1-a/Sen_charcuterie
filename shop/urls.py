# Dans ton fichier shop/urls.py
from django.urls import path
from .views import index, detail, verifier, Confirmation

urlpatterns = [
    path('', index, name='home'),
    path('produit/<int:myid>/', detail, name='detail'),
    path('verifier/', verifier, name='verifier'),
   
    path('confirmation/', Confirmation, name='Confirmation'), 
]