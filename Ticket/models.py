from django.db import models
from Transaction.models import Transaction
from Dab.models import Dab
from Carte.models import Carte

# Create your models here.
class Ticket(models.Model):
	numero_Ticket = models.CharField(max_length=10)
	id_Transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)
	id_Dab = models.ForeignKey(Dab,on_delete=models.CASCADE)
	id_Carte = models.ForeignKey(Carte,on_delete=models.CASCADE)

	def __str__(self):
		return self.numero_Ticket
