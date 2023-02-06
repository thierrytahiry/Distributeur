from django import forms
from .models import Compte

class CompteForm(forms.ModelForm):
	class Meta:
		model = Compte
		fields = ('numero_Compte','solde','id_Agence','id_Client')
		labels = {
			'numero_Compte':'Numéro de compte',
			'solde':'Solde',
			'id_Agence':'Agence',
			'id_Client':'Client',
		}
	def __init__(self, *args, **kwargs):
		super(CompteForm,self).__init__(*args, **kwargs)
		self.fields['id_Agence'].empty_label = "selectionnez"
		self.fields['id_Client'].empty_label = "selectionnez"