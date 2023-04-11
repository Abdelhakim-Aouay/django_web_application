from django.contrib import admin
from .models import Band, Listing

# Register your models here.
#admin.site.register(Band),
#admin.site.register(Listing),



class BandAdmin(admin.ModelAdmin): 
    # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre', 'active') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

class ListingAdmin(admin.ModelAdmin): 
    # nous insérons ces deux lignes..
    list_display = ('title', 'band') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Listing, ListingAdmin)