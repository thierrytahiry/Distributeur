from django.db import models
from Dab.models import Dab
from Operateur.models import Operateur
import datetime


# Create your models here.
class Ravitailler(models.Model):
	date_Ravitailler = models.DateTimeField(auto_now_add=True, verbose_name="date de ravitailler")
	nombre_20000_Inserer = models.IntegerField()
	nombre_10000_Inserer = models.IntegerField()
	nombre_5000_Inserer = models.IntegerField()
	id_Dab = models.ForeignKey(Dab,on_delete=models.CASCADE)
	id_Operateur = models.ForeignKey(Operateur,on_delete=models.CASCADE)

	def __str__(self):
		return self.date_Ravitailler