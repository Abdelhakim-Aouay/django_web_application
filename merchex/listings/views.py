from django.shortcuts import render, redirect
from . models import Band
from .form import ContactUsForm, BandForm, BandForm1
from django.core.mail import send_mail




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

def enregistrement(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method=='POST':
        myform=ContactUsForm(request.POST)
        if myform.is_valid():
            send_mail(
            subject=f'Message from {myform.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=myform.cleaned_data['message'],
            from_email=myform.cleaned_data['email'],
            recipient_list=['hkim_away@yahoo.fr'],)
        
    else:
        myform=ContactUsForm()   
    #print(request.POST.is_valid())
    return render(request, 'listings/enregistrement.html', {'my':myform})

def band_create(request):
    form = BandForm1()
    return render(request, 'listings/band_create.html',  {'form': form})
