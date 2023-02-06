from django import forms
from .models import Carte

class CarteForm(forms.ModelForm):
	class Meta:
		model = Carte
		fields = ('numero_Carte','code_Nip','etat_Carte','id_Compte','id_Type')
		labels = {
			'numero_Carte':'Numéro de carte',
			'etat_Carte':'Etat',
			'code_Nip':'NIP',
			'id_Compte':'Compte',
			'id_Type':'Type',
		}
			
	def __init__(self, *args, **kwargs):
		super(CarteForm,self).__init__(*args, **kwargs)
		self.fields['id_Compte'].empty_label = "selectionnez"
		self.fields['id_Type'].empty_label = "selectionnez"
		self.fields['etat_Carte'] = forms.ChoiceField(widget = forms.Select(), choices=([("Activer","Activer"),("Desactiver","Desactiver")]))
		self.fields['code_Nip'] = forms.CharField(widget=forms.PasswordInput)