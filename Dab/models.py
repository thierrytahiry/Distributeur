from django.db import models
from Agence.models import Agence

# Create your models here.
class Dab(models.Model):
	numero_Dab = models.CharField(max_length=10)
	lieu = models.CharField(max_length=50)
	nombre_Billet_20000 = models.IntegerField()
	nombre_Billet_10000 = models.IntegerField()
	nombre_Billet_5000 = models.IntegerField()
	id_Agence = models.ForeignKey(Agence,on_delete=models.CASCADE)

	def __str__(self):
		return self.numero_Dab
