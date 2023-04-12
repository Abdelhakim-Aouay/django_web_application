from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('', views.band_list, name="band-list"),
    path('<int:id>/', views.band_detail, name="band-detail"), # ajouter ce motif sous notre autre motif de groupes
    path('en', views.enregistrement, name="en"),
    path('add/', views.band_create, name='band-create'),
    path('addlist/', views.list_create, name='list-create'),
    path("listdetail/",views.list_detail, name="liste-detail"),
    path("listdetail/<int:id>/",views.list_list, name="liste-list"),
    path('update/<int:id>/', views.band_update, name='band-update'),
    path('listupdate/<int:id>', views.list_update, name='list-update'),
    path('delete/<int:id>', views.band_delete, name='band-delete'),
    path('listdelete/<int:id>', views.list_delete, name='list-delete'),   
]
