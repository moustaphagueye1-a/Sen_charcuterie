from django.shortcuts import render, get_object_or_404
from .models import Produit
from django.core.paginator import Paginator


def index(request):
    produits_list = Produit.objects.all()

    # On récupère la valeur du champ recherche
    item_name = request.GET.get('item-name', '')

    # Si l'utilisateur a tapé quelque chose
    if item_name:
        produits_list = produits_list.filter(nom__icontains=item_name)

    # Pagination (4 produits par page)
    paginator = Paginator(produits_list, 4)
    page = request.GET.get('page')
    produits = paginator.get_page(page)

    # On envoie aussi item_name au template
    return render(request, 'shop/index.html', {
        'produits': produits,
        'item_name': item_name
    })


def detail(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    return render(request, 'shop/detail.html', {'produit': produit})


def verifier(request):
    return render(request, 'shop/verifier.html')
