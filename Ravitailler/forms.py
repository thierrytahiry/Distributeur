from django import forms
from .models import Ravitailler

class RavitaillerForm(forms.ModelForm):
	class Meta:
		model = Ravitailler
		fields = ('nombre_20000_Inserer','nombre_10000_Inserer','nombre_5000_Inserer','id_Dab','id_Operateur')
		labels = {
			'nombre_20000_Inserer':'Nombre 20.000Ar Inséré',
			'nombre_10000_Inserer':'Nombre 10.000Ar Inséré',
			'nombre_5000_Inserer':'Nombre 5.000Ar Inséré',
			'id_Dab':'Dab',
			'id_Operateur':'Operateur',
		}
	def __init__(self, *args, **kwargs):
		super(RavitaillerForm,self).__init__(*args, **kwargs)
		self.fields['id_Dab'].empty_label = "selectionnez"
		self.fields['id_Operateur'].empty_label = "selectionnez"