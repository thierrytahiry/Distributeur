from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ('montant_Transaction','type_Transaction','id_Carte','id_Dab')
		labels = {
			'montant_Transaction':'Montant',
			'type_Transaction':'Type de transaction ',
			'id_Carte':'Numero carte',
			'id_Dab':'Numero de distributeur',
		}
	def __init__(self, *args, **kwargs):
		super(TransactionForm,self).__init__(*args, **kwargs)
		self.fields['id_Carte'].empty_label = "selectionnez"
		self.fields['id_Dab'].empty_label = "selectionnez"