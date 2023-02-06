from django.shortcuts import render,redirect
from .forms import CarteForm
from .models import Carte
from Transaction.models import Transaction
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate
from Dab.models import Dab

def Carte_list(request):
	context = {'carte_list': Carte.objects.all()}
	return render(request, "Carte/carte_list.html",context)

def formecarte(request):
	if request.method=='POST':
		Numcarte = request.POST['numCarte']
		if Numcarte:
			cartes = Carte.objects.filter(Q(numero_Carte=Numcarte))
			for carte in cartes:
				carteEtat = carte.etat_Carte
			if cartes and carteEtat == "Desactiver":
				messages.error(request,"Votre carte est bloquée, veuillez contacter le service d'information")
				return render(request, "Carte/code_nip.html",context)
			elif cartes:
				context = {'cartes': cartes}
				request.session['Numcarte'] = Numcarte
				return render(request, "Carte/code_nip.html",context)
			else:
				messages.error(request,"numéro de carte invalide")
	return render(request, "Carte/numero_compte.html")

def index(request):
	#
	# request.session.flush()
	context = {'distributeurs': Dab.objects.all()}
	if request.method=='POST':
		idDab = request.POST['idDab']
		request.session['idDab'] = idDab
		return render(request, "Carte/numero_compte.html")
	return render(request, "Carte/index.html",context)

def formenip(request):
	username = request.session.get("Numcarte")
	i = int(request.POST["count"])
	if request.method=='POST' and request.POST['Codenip'].isdigit():
		Codenip = request.POST['Codenip']
		cartes = Carte.objects.filter(Q(numero_Carte=username))
		for carte in cartes:
			codenip = carte.code_Nip
		if int(Codenip) == int(codenip):
			context = {'cartes': cartes}
			authenticate(username=username, password=codenip)
			return render(request, "Transaction/page_choix.html",context)
	messages.error(request,"Votre code NIP est incorrect")
	i = i + 1
	context = {"nb":i}
	if(i==3):
		Carte.objects.filter(numero_Carte=username).update(etat_Carte="Desactiver")
		# return redirect('/Carte/')
	return render(request, "Carte/code_nip.html",context)

def Carte_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = CarteForm()
		else:
			carte = Carte.objects.get(pk = id)
			form = CarteForm(instance = carte)
		return render(request, "Carte/carte_form.html", {'form':form})
	else:
		if id == 0:
			form = CarteForm(request.POST)
		else:
			carte = Carte.objects.get(pk = id)
			form = CarteForm(request.POST,instance = carte)
		if form.is_valid():
			code_Nip2 = request.POST['nip2']
			code_Nip = form.cleaned_data['code_Nip']
			if int(code_Nip2) == int(code_Nip):
				form.save()
			else:
				messages.error(request,"mess")
				return render(request, "Carte/carte_form.html", {'form':form})
		return redirect('/Carte/listCarte')
def Carte_delete(request, id):
	carte = Carte.objects.get(pk = id)
	carte.delete()
	return redirect('/Carte/listCarte')
