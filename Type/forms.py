from django import forms
from .models import Type

class TypeForm(forms.ModelForm):
	class Meta:
		model = Type
		fields = ('libelle_Type','limite_Montant_Jours','limite_Transaction_Jours','limite_Montant_Semaine','limite_Transaction_Semaine')
		labels = {
			'libelle_Type':'Libelle',
			'limite_Montant_Jours':'Montant limite J',
			'limite_Transaction_Jours':'limite de transaction J',
			'limite_Montant_Semaine':'Montant limite S',
			'limite_Transaction_Semaine':'limite de transaction S',
		}