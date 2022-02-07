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


def traitement(request):

    pForm = PersonForm2(request.POST)
    if pForm.is_valid():
        person = pForm.save()
        return render(request,'formulaire/affiche.html', {'person': person})
    else:
        return render(request, 'formulaire/name.html', {'form': pForm})

def index(request):
    liste = list(models.Person.objects.all())
    return render(request,'formulaire/index.html',{'liste': liste})