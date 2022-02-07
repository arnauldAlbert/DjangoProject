from django.urls import path

from . import views

urlpatterns = [
    path('formulaire', views.formulaire, name='formulaire'),
    path('traitement/', views.traitement, name='affiche'),
    path('', views.index, name='index'),
]
