from django import forms
from .models import Agence

class AgenceForm(forms.ModelForm):
	class Meta:
		model = Agence
		fields = ('nom_Agence','direction','lieu_Agence','code_Agence','telephone_Agence')
		labels = {
			'nom_Agence':'Nom d\'Agence',
			'lieu_Agence':'Lieu',
			'code_Agence':'Code d\'Agence',
			'telephone_Agence':'Numéro telephone',
		}