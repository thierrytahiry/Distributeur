from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ('nom','prenom','telephone','CIN','adresse','dateNaissance')
		labels = {
			'nom':'Nom',
			'prenom':'Prenom',
			'telephone':'Numéro telephone',
			'adresse':'Adresse',
			'dateNaissance':'Date de naissance',
		}
	def __init__(self, *args, **kwargs):
		super(ClientForm,self).__init__(*args, **kwargs)
		self.fields['dateNaissance'] = forms.DateField(widget = forms.TextInput(attrs={'type':'date'}))