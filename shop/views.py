from django.shortcuts import render, get_object_or_404  # <--- Ne pas oublier get_object_or_404
from .models import Produit
from django.core.paginator import Paginator

def index(request):
    produits_list = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produits_list = produits_list.filter(nom__icontains=item_name)

    paginator = Paginator(produits_list, 4) 
    page = request.GET.get('page') 
    produits = paginator.get_page(page) 

    return render(request, 'shop/index.html', {'produits': produits})

def detail(request, myid):
    # Maintenant que l'import est fait, ça va marcher
    produit = get_object_or_404(Produit, id=myid)
    return render(request, 'shop/detail.html', {'produit': produit})
def verifier(request):
    return render(request, 'shop/verifier.html')    