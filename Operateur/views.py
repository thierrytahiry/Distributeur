from django.shortcuts import render,redirect
from .forms import OperateurForm
from .models import Operateur
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages

def login_view(request):

	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		if username and password:
			operateurs = Operateur.objects.filter(Q(username=username))
			
			if username == "admin" and password == "prosper":
				request.session['email'] = "admin@admin.com"
				request.session['prenom'] = "admin"
				return redirect('/Transaction/pageChart')

			if operateurs:
				for operateur in operateurs:
					Username = operateur.username
					Password = operateur.password
					prenom = operateur.prenom_Operateur
					email = operateur.email_Operateur
				if Username == username and Password == password:
					request.session['email'] = email
					request.session['prenom'] = prenom
					return redirect('/Transaction/pageChart')

				if Username == username and Password != password:
					messages.error(request,"Mot de passe invalide")
			else:
				messages.error(request,"Operateur n'existe pas")
		else:
			messages.error(request,"Veuillez compléter les champs")
	request.session.flush()
	return render(request, 'Operateur/login.html')

def Operateur_list(request):
	context = {'operateur_list': Operateur.objects.all()}
	return render(request, "Operateur/operateur_list.html",context)

def Operateur_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = OperateurForm()
		else:
			operateur = Operateur.objects.get(pk = id)
			form = OperateurForm(instance = operateur)
		return render(request, "Operateur/operateur_form.html", {'form':form})
	else:
		if id == 0:
			form = OperateurForm(request.POST)
		else:
			operateur = Operateur.objects.get(pk = id)
			form = OperateurForm(request.POST,instance = operateur)
		if form.is_valid():
			form.save()
		return redirect('/Operateur/listOperateur')

def Operateur_delete(request, id):
	operateur = Operateur.objects.get(pk = id)
	operateur.delete()
	return redirect('/Operateur/listOperateur')
