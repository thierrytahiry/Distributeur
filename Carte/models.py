from django.db import models
from Compte.models import Compte
from Type.models import Type

# Create your models here.
class Carte(models.Model):
	numero_Carte = models.CharField(max_length=19)
	code_Nip = models.CharField(max_length=6)
	etat_Carte = models.CharField(max_length=19)
	id_Compte = models.ForeignKey(Compte,on_delete=models.CASCADE)
	id_Type = models.ForeignKey(Type,on_delete=models.CASCADE)

	def __str__(self):
		return self.numero_Carte