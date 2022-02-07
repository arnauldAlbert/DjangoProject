from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        chaine =  f"Nom : {self.name} \n prénom : {self.firstname}"
        return chaine
