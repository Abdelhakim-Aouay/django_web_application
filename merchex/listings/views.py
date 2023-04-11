from django.shortcuts import render
from . models import Band

def hello(request):
    bands=Band.objects.all()
    return render(request, 'listings/hello.html', {"data": bands})


# listings/views.py


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band =Band.objects.filter(id=id).values()
    print(band)    
    
    return render(request,'listings/band_detail.html',{'id': id, 'band': band}) # nous passons l'id au modè