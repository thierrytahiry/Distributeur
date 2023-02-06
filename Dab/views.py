from django.shortcuts import render,redirect
from .forms import DabForm
from .models import Dab
from Ravitailler.forms import RavitaillerForm
from Operateur.models import Operateur
from django.db.models import Q

def Dab_list(request):
	context = {'dab_list': Dab.objects.all()}
	return render(request, "Dab/dab_list.html",context)

def Dab_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = DabForm()
		else:
			dabs = Dab.objects.filter(id=id)
			for dab in dabs:
				dabId = dab.id
				dabNum = dab.numero_Dab
			form = RavitaillerForm()
			prenom = request.session.get("prenom","Vide")

			operateurs = Operateur.objects.filter(Q(prenom_Operateur=prenom))
			
			for operateur in operateurs:
				prenom = operateur.prenom_Operateur
				operateurId = operateur.id
			context = {
				'dabId':dabId,
				'form':form,
				'dabNum':dabNum,
				'prenom':prenom,
				'operateurId':operateurId
			}
			return render(request, "Ravitailler/ravitailler_form.html", context)
	else:
		if id == 0:
			form = DabForm(request.POST)
		else:
			dab = Dab.objects.get(pk = id)
			form = DabForm(request.POST,instance = dab)
		if form.is_valid():
			form.save()
		return redirect('/Dab/listDab')
	return render(request, "Dab/dab_form.html" , {'form':form})

def Dab_Edit_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = DabForm()
		else:
			dab = Dab.objects.get(pk = id)
			form = DabForm(instance = dab)
		return render(request, "Dab/dab_form.html", {'form':form})
	else:
		if id == 0:
			form = DabForm(request.POST)
		else:
			dab = Dab.objects.get(pk = id)
			form = DabForm(request.POST,instance = dab)
		if form.is_valid():
			form.save()
		return redirect('/Dab/listDab')

def Dab_delete(request, id):
	dab = Dab.objects.get(pk = id)
	dab.delete()
	return redirect('/Dab/listDab')
