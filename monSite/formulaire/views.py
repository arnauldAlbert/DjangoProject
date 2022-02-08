from django.shortcuts import render
from  django.http import HttpResponseRedirect
from . import models
from django.template import loader

from .forms import PersonForm2


# Create your views here.

def formulaire(request):
    if request.method == "POST":
        form = PersonForm2(request)
        if form.is_valid():

            return HttpResponseRedirect("/thanks/")
    else:
        form = PersonForm2()
    return render(request, 'formulaire/name.html', {'form': form})


def traitementUpdate(request, id):
    pForm = PersonForm2(request.POST)
    if pForm.is_valid():
        person = pForm.save(commit=False)
        person.id=id
        p = pForm.save()
        # return render(request,'formulaire/affiche.html', {'person': person})
        """ permet de faire la redirection vers la page d'accueil """
        return HttpResponseRedirect("/formulaire/")
    else:
        return render(request, 'formulaire/name.html', {'form': pForm})

def traitement(request):
    pForm = PersonForm2(request.POST)
    if pForm.is_valid():
        person = pForm.save()
        """ permet de faire la redirection vers la page d'accueil"""
        return HttpResponseRedirect("/formulaire/")
    else:
        return render(request, 'formulaire/name.html', {'form': pForm})

def index(request):
    liste = list(models.Person.objects.all())
    return render(request,'formulaire/index.html',{'liste': liste})

def update(request, id):
    p = models.Person.objects.get(pk=id)
    pForm = PersonForm2(None, instance = p)
    return render(request, 'formulaire/update.html', {'form': pForm, 'id' : id})

def delete(request, id):
    p = models.Person.objects.get(pk=id)
    p.delete()
    return HttpResponseRedirect("/formulaire/")