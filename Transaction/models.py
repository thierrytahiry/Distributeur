from django.db import models
import datetime
from Carte.models import Carte
from Dab.models import Dab

# Create your models here.
class Transaction(models.Model):
	montant_Transaction = models.IntegerField()
	type_Transaction = models.CharField(max_length=50)
	# numero_Transaction = models.CharField(max_length=50,null=True)
	date_Transaction = models.DateTimeField(auto_now_add=True, verbose_name="date de Transaction")
	id_Carte = models.ForeignKey(Carte,on_delete=models.CASCADE,)
	id_Dab = models.ForeignKey(Dab,on_delete=models.CASCADE)

	def __str__(self):
		return self.type_Transaction

