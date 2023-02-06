from django.shortcuts import render,redirect
from .forms import CompteForm
from .models import Compte

def Compte_list(request):
	context = {'compte_list': Compte.objects.all()}
	return render(request, "Compte/compte_list.html",context)


def Compte_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = CompteForm()
		else:
			compte = Compte.objects.get(pk = id)
			form = CompteForm(instance = compte)
		return render(request, "Compte/compte_form.html", {'form':form})
	else:
		if id == 0:
			form = CompteForm(request.POST)
		else:
			compte = Compte.objects.get(pk = id)
			form = CompteForm(request.POST,instance = compte)
		if form.is_valid():
			form.save()
		return redirect('/Compte/listCompte')

def Compte_delete(request, id):
	compte = Compte.objects.get(pk = id)
	compte.delete()
	return redirect('/Compte/listCompte')
