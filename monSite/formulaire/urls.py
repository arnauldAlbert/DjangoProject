from django.urls import path

from . import views

urlpatterns = [
    path('formulaire', views.formulaire, name='formulaire'),
    path('traitement/', views.traitement, name='traitement'),
    path('<int:id>/traitement/', views.traitementUpdate, name='traitement_update'),
    path('', views.index, name='index'),
    path('<int:id>/update/',views.update,name="update"),
    path('<int:id>/delete/',views.delete,name="delete"),
]
