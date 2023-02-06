from django.db import models

# Create your models here.
class Agence(models.Model):
	lieu_Agence = models.CharField(max_length=50)
	code_Agence = models.CharField(max_length=10)
	nom_Agence = models.CharField(max_length=50)
	direction = models.CharField(max_length=50)
	telephone_Agence = models.CharField(max_length=15)

	def __str__(self):
		return self.nom_Agence
