from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Commande
from django.core.paginator import Paginator

def index(request):
    produits_list = Produit.objects.all()
    item_name = request.GET.get('item-name', '')
    if item_name:
        produits_list = produits_list.filter(nom__icontains=item_name)

    paginator = Paginator(produits_list, 4)
    page = request.GET.get('page')
    produits = paginator.get_page(page)

    return render(request, 'shop/index.html', {'produits': produits, 'item_name': item_name})

def detail(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    return render(request, 'shop/detail.html', {'produit': produit})

def verifier(request):
    if request.method == "POST":
        # Récupération des données du formulaire
        items = request.POST.get('items')
        total = request.POST.get('total')

        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        region = request.POST.get('region')
        commune = request.POST.get('commune')
        adresse = request.POST.get('adresse')

        # Sauvegarde en base de données
        com = Commande(
            items=items, total=total, nom=nom, email=email, 
            telephone=telephone, region=region, 
            commune=commune, adresse=adresse
        )
        com.save()
        return redirect('Confirmation') # Redirige vers la page de confirmation  après succès

    return render(request, 'shop/verifier.html')
def Confirmation(request):
    info = Commande.objects.all()  # Récupère la dernière commande passée
    for item in info :
        nom = item.nom
    return render(request, 'shop/confirmation.html',{'nom': nom})