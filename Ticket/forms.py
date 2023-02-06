from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('numero_Ticket','id_Transaction','id_Dab','id_Carte')
		labels = {
			'numero_Ticket':'Numéro de Ticket',
			'id_Transaction':'Transaction',
			'id_Dab':'Dab',
			'id_Carte':'Carte',
		}
	def __init__(self, *args, **kwargs):
		super(TicketForm,self).__init__(*args, **kwargs)
		self.fields['id_Transaction'].empty_label = "selectionnez"
		self.fields['id_Dab'].empty_label = "selectionnez"
		self.fields['id_Carte'].empty_label = "selectionnez"