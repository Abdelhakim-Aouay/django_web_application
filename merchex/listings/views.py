from django.shortcuts import render
from . models import Band

def hello(request):
    bands=Band.objects.all()
    return render(request, 'listings/hello.html', {"data": bands})


# listings/views.py


def band_list(request):  # notez le paramètre id supplémentaire
    bands =Band.objects.all()
    return render(request,'listings/band_list.html',{'bands': bands}) # nous passons l'id au modè


# listings/views.py


def band_detail(request, id):
    band =Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band}) # nous passons l'id au modèle
