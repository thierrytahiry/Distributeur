from django.shortcuts import render,redirect
from .forms import AgenceForm
from .models import Agence

def Agence_list(request):
	context = {'agence_list': Agence.objects.all()}
	return render(request, "Agence/agence_list.html",context)


def Agence_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = AgenceForm()
		else:
			agence = Agence.objects.get(pk = id)
			form = AgenceForm(instance = agence)
		return render(request, "Agence/agence_form.html", {'form':form})
	else:
		if id == 0:
			form = AgenceForm(request.POST)
		else:
			agence = Agence.objects.get(pk = id)
			form = AgenceForm(request.POST,instance = agence)
		if form.is_valid():
			form.save()
		return redirect('/Agence/listAgence')


def Agence_delete(request, id):
	agence = Agence.objects.get(pk = id)
	agence.delete()
	return redirect('/Agence/listAgence')