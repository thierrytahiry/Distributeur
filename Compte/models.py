from django.db import models
from Agence.models import Agence
from Client.models import Client

# Create your models here.
class Compte(models.Model):
	numero_Compte = models.CharField(max_length=20)
	solde = models.IntegerField()
	id_Agence = models.ForeignKey(Agence,on_delete=models.CASCADE)
	id_Client = models.ForeignKey(Client,on_delete=models.CASCADE)

	def __str__(self):
		return self.numero_Compte
