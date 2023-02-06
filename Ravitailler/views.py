from django.shortcuts import render,redirect
from .forms import RavitaillerForm
from .models import Ravitailler
from Dab.models import Dab
from django.db.models import Q

def Ravitailler_list(request):
	context = {'ravitailler_list': Ravitailler.objects.all()}
	return render(request, "Ravitailler/ravitailler_list.html",context)
	
def Ravitailler_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = RavitaillerForm()
		else:
			ravitailler = Ravitailler.objects.get(pk = id)
			form = RavitaillerForm(instance = ravitailler)
		return render(request, "Ravitailler/ravitailler_form.html", {'form':form})
	else:
		if id == 0:
			form = RavitaillerForm(request.POST)
		else:
			#begin history dab and insert money
			ravitailler = Ravitailler.objects.get(pk = id)
			form = RavitaillerForm(request.POST,instance = ravitailler)

		if form.is_valid():
			form.save()
			dabId = int(request.POST['id_Dab'])
			nb20Entree = int(request.POST['nombre_20000_Inserer'])
			nb10Entree = int(request.POST['nombre_10000_Inserer'])
			nb5Entree = int(request.POST['nombre_5000_Inserer'])

			dabs = Dab.objects.filter(Q(id=dabId))
			for dab in dabs:
				nb20 = dab.nombre_Billet_20000
				nb10 = dab.nombre_Billet_10000
				nb5 = dab.nombre_Billet_5000

			nb20ttl = nb20Entree + nb20
			nb10ttl = nb10Entree + nb10
			nb5ttl = nb5Entree + nb5
			Dab.objects.filter(id=dabId).update(nombre_Billet_20000=nb20ttl, nombre_Billet_10000=nb10ttl, nombre_Billet_5000=nb5ttl)
		else:
			return redirect('/Dab/listDab')
		return redirect('/Ravitailler/listRavitailler')

def Ravitailler_delete(request, id):
	ravitailler = Ravitailler.objects.get(pk = id)
	ravitailler.delete()
	return redirect('/Ravitailler/listRavitailler')
