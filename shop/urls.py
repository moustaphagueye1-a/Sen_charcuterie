from django.urls import path
from shop.views import index, detail, verifier 

urlpatterns = [
    path('', index, name='home'),
    # Correction : On ajoute les chevrons et le slash final
    path('<int:myid>/', detail, name='detail'), 
    path('verifier', verifier, name='Detail_achat'),
]