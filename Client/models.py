from django.db import models

# Create your models here.
class Client(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	telephone = models.CharField(max_length=15)
	CIN = models.CharField(max_length=12)
	adresse = models.CharField(max_length=50)
	dateNaissance = models.DateField()

	def __str__(self):
		return self.nom
