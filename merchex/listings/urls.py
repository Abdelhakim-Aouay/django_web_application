from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('', views.band_list, name="band-list"),
    path('<int:id>/', views.band_detail, name="band-detail"), # ajouter ce motif sous notre autre motif de groupes

    
]
