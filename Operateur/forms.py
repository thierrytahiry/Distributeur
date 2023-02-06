from django import forms
from .models import Operateur

class OperateurForm(forms.ModelForm):
	class Meta:
		model = Operateur
		fields = ('nom_Operateur','prenom_Operateur','telephone_Operateur','email_Operateur','username','password','date_Naissance_Operateur')
		labels = {
			'nom_Operateur':'Nom',
			'prenom_Operateur':'Prenom ',
			'telephone_Operateur':'Téléphone',
			'email_Operateur':'Email',
			'username':'Pseudo',
			'password':'Mot de passe',
			'date_Naissance_Operateur':'Naissance',
		}
	def __init__(self, *args, **kwargs):
		super(OperateurForm,self).__init__(*args, **kwargs)
		self.fields['date_Naissance_Operateur'] = forms.DateField(widget = forms.TextInput(attrs={'type':'date'}))
		self.fields['password'] = forms.CharField(widget=forms.PasswordInput)

	def clean_email(self):
		email = self.cleaned_data.get('email_Operateur')
		if email:
			email_Operateur_qs = Operateur.objects.filter(email_Operateur=email)
		if email_Operateur_qs.exists():
			raise forms.ValidationError(
				"Email déjà existe"
			)
		return email