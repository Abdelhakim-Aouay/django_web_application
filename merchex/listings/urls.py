from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('<int:id>/', views.band_detail), # ajouter ce motif sous notre autre motif de groupes

    
]
