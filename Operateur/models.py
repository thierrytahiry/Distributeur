from django.db import models

# Create your models here.
class Operateur(models.Model):
	nom_Operateur = models.CharField(max_length=50)
	prenom_Operateur = models.CharField(max_length=20)
	telephone_Operateur = models.CharField(max_length=14)
	email_Operateur = models.EmailField(max_length=70,null=True,blank=True,unique=True)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	date_Naissance_Operateur = models.DateField()

	def __str__(self):
		return self.prenom_Operateur