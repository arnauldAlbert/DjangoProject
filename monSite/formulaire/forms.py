from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class PersonForm(forms.Form):
    name = forms.CharField(label="Nom", max_length = 100)
    firstname = forms.CharField(label="prénom", max_length=100)
    age = forms.IntegerField(label="age")


class PersonForm2(ModelForm):
    class Meta:
        model = models.Person
        fields = ('name', 'firstname', 'birthday', 'email')
        labels = {
            'name': _('Nom '),
            'firstname': _('Prénom')
        }



