from django.db import models

# Create your models here.
class Type(models.Model):
	libelle_Type = models.CharField(max_length=50)
	limite_Montant_Jours = models.IntegerField()
	limite_Transaction_Jours = models.IntegerField()
	limite_Montant_Semaine = models.IntegerField(null=True)
	limite_Transaction_Semaine = models.IntegerField(null=True)


	def __str__(self):
		return self.libelle_Type
