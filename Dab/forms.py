from django import forms
from .models import Dab

class DabForm(forms.ModelForm):
	class Meta:
		model = Dab
		fields = ('numero_Dab','lieu','nombre_Billet_20000','nombre_Billet_10000','nombre_Billet_5000','id_Agence')
		labels = {
			'numero_Dab':'Numéro de Dab',
			'lieu':'Lieu ',
			'nombre_Billet_20000':'Nombre de 20 000 Ar',
			'nombre_Billet_10000':'Nombre de 10 000 Ar',
			'nombre_Billet_5000':'Nombre de 5 000 Ar',
			'id_Agence':'Agence',
		}
	def __init__(self, *args, **kwargs):
		super(DabForm,self).__init__(*args, **kwargs)
		self.fields['id_Agence'].empty_label = "selectionnez"