from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from datetime import datetime
from .forms import TransactionForm
from .models import Transaction
from Carte.models import Carte
from Compte.models import Compte
from Ticket.models import Ticket
from Type.models import Type
from Dab.models import Dab
from django.db.models import Q
from django.contrib import messages
from django.db.models import Avg, Max, Min


def Transaction_list(request):
	context = {'transaction_list': Transaction.objects.all()}
	return render(request, "Transaction/transaction_list.html",context)

def PageRelever(request):
	
	numcarte = request.session.get("Numcarte")
	if numcarte:
		cartes = Carte.objects.filter(Q(numero_Carte=numcarte))
		for carte in cartes:
			carteId = carte.id
		transactions = Transaction.objects.filter(Q(id_Carte=carteId))
		context = {'transaction_list': transactions,'date': datetime.now()}
		return render(request, "Transaction/page_relever.html",context)
	else:
		return redirect('/Transaction/pageChoix')


def PageChoix(request):
	numcarte_sess = request.session.get("Numcarte")
	return render(request, "Transaction/page_choix.html",{'numcarte_sess': numcarte_sess})

def PageRetirer(request):
	numcarte_sess = request.session.get("Numcarte")
	cartes = Carte.objects.all()
	context = {'numcarte_sess': request.session.get("Numcarte"), 'cartes': Carte.objects.all()}
	return render(request, "Transaction/page_retirer.html", context)

def AutreMontant(request):
	numcarte_sess = request.session.get("Numcarte")
	cartes = Carte.objects.all()
	context = {'numcarte_sess': request.session.get("Numcarte"), 'cartes': Carte.objects.all()}
	return render(request, "Transaction/page_autre_montant.html", context)

def PageDepot(request):
	numcarte_sess = request.session.get("Numcarte")
	cartes = Carte.objects.all()
	context = {'numcarte_sess': request.session.get("Numcarte"), 'cartes': Carte.objects.all()}
	return render(request, "Transaction/page_depot.html", context)

def PageReçus(request):
	return render(request, 'Transaction/page_reçus.html')

def PageSolde(request):
	numcarte = request.session.get("Numcarte")

	cartes = Carte.objects.filter(Q(numero_Carte=numcarte))
	for carte in cartes:
		carteIdCompte = carte.id_Compte
		carteId = carte.id
		carteNUM = carte.numero_Carte

	comptes = Compte.objects.filter(Q(numero_Compte=carteIdCompte))
	for compte in comptes:
		soldeCompte = compte.solde

	date = datetime.now()
	context = {
		'soldeCompte': soldeCompte, 
		'idCarte': carteId,
		'numCompte':carteIdCompte,
		'carteNUM':carteNUM,
		'date':date
		}
	return render(request, "Transaction/page_solde.html", context)


def Transaction_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = TransactionForm()
		else:
			transaction = Transaction.objects.get(pk = id)
			form = TransactionForm(instance = transaction)
		return render(request, "Transaction/Transaction_form.html", {'form':form})
	else:

	#begin update solde

		dabId = request.session.get("idDab")
		numcarte = request.session.get("Numcarte")
		
		dabs = Dab.objects.filter(Q(id=dabId))
		for dab in dabs:
			lieuDab = dab.lieu
			nb20 = dab.nombre_Billet_20000
			nb10 = dab.nombre_Billet_10000
			nb5 = dab.nombre_Billet_5000
			numDab = dab.numero_Dab
		cartes = Carte.objects.filter(Q(numero_Carte=numcarte))

		for carte in cartes:
			carteId = carte.id
			carteNumCompte = carte.id_Compte
			carteLibelleType = carte.id_Type

		comptes = Compte.objects.filter(Q(numero_Compte=carteNumCompte))
		for compte in comptes:
			soldeCompte = compte.solde
			compteId = compte.id
			clientCompte = compte.id_Client

		types = Type.objects.filter(Q(libelle_Type=carteLibelleType))
		for typev in types:
			montantLimiteJ = typev.limite_Montant_Jours
			montantLimiteS = typev.limite_Montant_Semaine
			transactionLimiteJ = typev.limite_Transaction_Jours
			transactionLimiteS = typev.limite_Transaction_Semaine
			
		if int(request.POST['montant_Transaction']) != 0 and int(request.POST['montant_Transaction']) % 5000 == 0:

			montantTransition = request.POST['montant_Transaction']
			montantTrans = int(montantTransition)

			#begin retrait
			if request.POST['type_Transaction'] == "Retrait":

				jours = 0
				x = 0
				semaine = 0
				sommeMontantJ = 0
				sommeMontantM = 0
				montantTTLJ = 0
				montantTTLM = 0
				transactions = Transaction.objects.filter(Q(id_Carte=carteId))
				for trans in transactions:
					dates = trans.date_Transaction
					montant = trans.montant_Transaction
					dateSplit = datetime.date(dates)
					dateDern = str(dateSplit).split("-")
					dateNow = str(datetime.date(datetime.now())).split("-")
					transactionType = trans.type_Transaction
					transactionId = trans.id
					#all date
					J_Dern = int(dateDern[2])
					M_Dern = dateDern[1]
					A_Dern = dateDern[0]

					#Date current
					J_Now = int(dateNow[2])
					M_Now = dateNow[1]
					A_Now = dateNow[0]
					
					if M_Dern == 1:
						Jours = 31
					elif M_Dern == 2:
						Jours = 28
					elif M_Dern == 3:
						Jours = 31
					elif M_Dern == 4:
						Jours = 30
					elif M_Dern == 5:
						Jours = 31
					elif M_Dern == 6:
						Jours = 30
					elif M_Dern == 7:
						Jours = 31
					elif M_Dern == 8:
						Jours = 31
					elif M_Dern == 9:
						Jours = 30
					elif M_Dern == 10:
						Jours = 31
					elif M_Dern == 11:
						Jours = 30
					elif M_Dern == 12:
						Jours = 31
					else :
						Jours = 29
					print(dates)
					# print(J_Dern)
					if datetime.date(dates) <= datetime.date(datetime.now()) and transactionType == "Retrait":
						if J_Dern == J_Now:
							jours = jours + 1
							if montant != 0:
								montantTTLJ = montantTTLJ + montant
							sommeMontantJ = montantTTLJ + montantTrans

							if jours%transactionLimiteJ == 0:
								messages.error(request,"Le retrait d'argent est limité %d fois par jour" % transactionLimiteJ)
								return redirect('/Transaction/pageChoix')

							if sommeMontantJ > montantLimiteJ:
								messages.error(request,"Le retrait d'argent est limité %d Ar par jour" % montantLimiteJ)
								return redirect('/Transaction/pageChoix')
						if J_Dern > J_Now :
							NbJ = (J_Now + Jours) - J_Dern
						else :
							NbJ = J_Now - J_Dern
						x = x + 1
						i = 0
						# print(NbJ)
						if NbJ <= 7 and x%transactionLimiteS == 0:
							while i < 7:
								if M_Dern == M_Now and A_Dern == A_Now and i < 7:
									semaine = semaine + 1
									if montant != 0:
										montantTTLM = montantTTLM + montant
									sommeMontantM = montantTTLM + montantTrans
									if semaine%transactionLimiteS == 0:
										messages.error(request,"Le retrait d'argent est limité %d fois par semaine" % transactionLimiteS)
										return redirect('/Transaction/pageChoix')
									if sommeMontantM > montantLimiteS:
										messages.error(request,"Le retrait d'argent est limité %d Ar par semaine" % montantLimiteS)
										return redirect('/Transaction/pageChoix')
								i = i + 1

				if montantTrans > montantLimiteJ:
					# print(montantTrans)
					messages.error(request,"Le retrait d'argent est limité %d Ar par jour" % montantLimiteJ)
					return redirect('/Transaction/pageChoix')

				#///////////////////////////////////////////////////////
				restSolde = soldeCompte - montantTrans
				bool = False
				montantDab = nb20*20000 + nb10*10000 + nb5*5000

				nb20reel = montantTrans/20000
				nb10reel = montantTrans/10000
				nb5reel =  montantTrans/5000

				nb20entier = int(nb20reel)
				nb10entier = int(nb10reel)
				nb5entier = int(nb5reel)
				if soldeCompte >= montantTrans:
					if montantDab >= montantTrans:
						for nb20Sortie in range(nb20entier, -1, -1):
							for nb10Sortie in range(nb10entier, -1, -1):
								for nb5Sortie in range(nb5entier, -1, -1):
									montantsortie = nb20Sortie*20000 + nb10Sortie*10000 + nb5Sortie*5000
									if montantsortie == montantTrans:
										if nb20Sortie <= nb20 and nb10Sortie <= nb10 and nb5Sortie <= nb5:
											bool = True
											nb20reste = nb20 - nb20Sortie
											nb10reste = nb10 - nb10Sortie
											nb5reste = nb5 - nb5Sortie
											Dab.objects.filter(id=dabId).update(nombre_Billet_20000=nb20reste, nombre_Billet_10000=nb10reste, nombre_Billet_5000=nb5reste)
											Compte.objects.filter(id=compteId).update(solde=restSolde)
											ttl20 = nb20Sortie * 20000
											ttl10 = nb10Sortie * 10000
											ttl5 = nb5Sortie * 5000
											ttls = ttl20 + ttl10 + ttl5
											break
								if bool == True:
									break
							if bool == True:
								break

						if id == 0:
							form = TransactionForm(request.POST)
						else:
							transaction = Transaction.objects.get(pk = id)
							form = TransactionForm(request.POST,instance = transaction)
						if form.is_valid():
							form.save()
							context = {"idMax":Transaction.objects.all().aggregate(Max('id')),"numDab":numDab,"carteId":carteId,"Solde":restSolde,"nb20Sortie":nb20Sortie, "nb10Sortie":nb10Sortie, "nb5Sortie":nb5Sortie, "ttl20":ttl20, "ttl10":ttl10,"ttl5":ttl5, "ttls":ttls, "mess":"VOUS AVEZ RECUS","dateNow":datetime.now(),"numcarte":numcarte,"NumCompte":carteNumCompte,"transactionType":"Retrait","dabid":dabId,'lieuDab':lieuDab,"clientCompte":clientCompte}
						return render(request, "Transaction/page_reçus.html", context)
					else:
						messages.error(request,"Montant dans le DAB est %d Ar" % montantDab)
						return redirect('/Transaction/pageChoix')
				else:
					messages.error(request,"Votre solde est insuffisante. Solde actuel %d Ar" % soldeCompte)
					return redirect('/Transaction/pageChoix')
			#end retrait

			#begin depot
			else:
				Soldettl = soldeCompte + montantTrans
				nb20Entree = int(request.POST['nb20Entree'])
				nb10Entree = int(request.POST['nb10Entree'])
				nb5Entree = int(request.POST['nb5Entree'])
				ttl20 = nb20Entree * 20000
				ttl10 = nb10Entree * 10000
				ttl5 = nb5Entree * 5000
				ttls = ttl20 + ttl10 + ttl5

				nb20ttl = nb20 + nb20Entree
				nb10ttl = nb10 + nb10Entree
				nb5ttl = nb5 + nb5Entree
			
				Dab.objects.filter(id=dabId).update(nombre_Billet_20000=nb20ttl, nombre_Billet_10000=nb10ttl, nombre_Billet_5000=nb5ttl)
				Compte.objects.filter(id=compteId).update(solde=Soldettl)
				if id == 0:
					form = TransactionForm(request.POST)
				else:
					transaction = Transaction.objects.get(pk = id)
					form = TransactionForm(request.POST,instance = transaction)
				if form.is_valid():
					form.save()
					context = {"idMax":Transaction.objects.all().aggregate(Max('id')),"numDab":numDab,"carteId":carteId,"Solde":Soldettl,"nb20Sortie":nb20Entree, "nb10Sortie":nb10Entree, "nb5Sortie":nb5Entree, "ttl20":ttl20, "ttl10":ttl10,"ttl5":ttl5, "ttls":ttls, "mess":"VOUS AVEZ DEPOSE","dateNow":datetime.now(),"numcarte":numcarte,"NumCompte":carteNumCompte,"transactionType":"Dépôt","dabid":dabId,"lieuDab":lieuDab,"clientCompte":clientCompte}
				return render(request, "Transaction/page_reçus.html", context)
			return redirect('/Transaction/pageRetirer')
			#end depot
		
		elif request.POST['type_Transaction'] == "Consulté le solde":
			if id == 0:
				form = TransactionForm(request.POST)
			else:
				transaction = Transaction.objects.get(pk = id)
				form = TransactionForm(request.POST,instance = transaction)
			if form.is_valid():
				form.save()
				context = {"idMax":Transaction.objects.all().aggregate(Max('id')),"numDab":numDab,"carteId":carteId,"soldeActuel":soldeCompte,"nb20Sortie":0, "nb10Sortie":0, "nb5Sortie":0, "dateNow":datetime.now(),"numcarte":numcarte,"NumCompte":carteNumCompte,"transactionType":"Consulté le solde","dabid":dabId,'lieuDab':lieuDab,"clientCompte":clientCompte}
				return render(request, "Transaction/page_reçus.html", context)

		elif int(request.POST['montant_Transaction']) == 0 and request.POST['type_Transaction'] == "Dépôt":
			messages.error(request,"Vérifiez votre montant")
			return redirect('/Transaction/pageDepot')

		elif (int(request.POST['montant_Transaction'])%5000 != 0 or int(request.POST['montant_Transaction']) == 0) and request.POST['typeautre'] == "typeautre" and request.POST['type_Transaction'] == "Retrait":
			messages.error(request,"Vérifiez votre montant")
			return redirect('/Transaction/autreMontant')
		else:
			messages.error(request,"mess")
			return redirect('/Transaction/pageRetirer')

def Transaction_delete(request, id):
	transaction = Transaction.objects.get(pk = id)
	transaction.delete()
	return redirect('/Transaction/listTransaction')

def PageChart(request):
	# for trans in transactions:
	Retraits = Transaction.objects.filter(Q(type_Transaction='Retrait'))
	Depots = Transaction.objects.filter(Q(type_Transaction='Dépôt'))
	retr = 0
	dep = 0
	retraitMois = 0
	depotMois = 0
	for retrait in Retraits:
		dates = retrait.date_Transaction
		retraitType = retrait.type_Transaction
		dateSplit = datetime.date(dates)
		dateDern = str(dateSplit).split("-")
		dateNow = str(datetime.date(datetime.now())).split("-")
		#all date
		M_Dern = dateDern[1]
		#Date current
		M_Now = dateNow[1]
		if datetime.date(dates) == datetime.date(datetime.now()):
			retr = retr + 1

		if M_Dern == M_Now:
			retraitMois = retraitMois + 1

	for depot in Depots:
		dates = depot.date_Transaction
		depotType = depot.type_Transaction
		dateSplit = datetime.date(dates)
		dateDern = str(dateSplit).split("-")
		dateNow = str(datetime.date(datetime.now())).split("-")
		#all date
		M_Dern = dateDern[1]
		#Date current
		M_Now = dateNow[1]
		if datetime.date(dates) == datetime.date(datetime.now()):
			dep = dep + 1

		if M_Dern == M_Now:
			depotMois = depotMois + 1

		if int(M_Now) == 1:
			Jours = 'Janvier'
		elif int(M_Now) == 2:
			Jours = 'Février'
		elif int(M_Now) == 3:
			Jours = 'Mars'
		elif int(M_Now) == 4:
			Jours = 'Avril'
		elif int(M_Now) == 5:
			Jours = 'Mais'
		elif int(M_Now) == 6:
			Jours = 'Juin'
		elif int(M_Now) == 7:
			Jours = 'Juillet'
		elif int(M_Now) == 8:
			Jours = 'Août'
		elif int(M_Now) == 9:
			Jours = 'Septembre'
		elif int(M_Now) == 10:
			Jours = 'Octobre'
		elif int(M_Now) == 11:
			Jours = 'Novembre'
		else:
			Jours = 'Décembre'

	context = {'retrait': retr,'depot':dep,'type1':2,'type2':2,'retraitMois':retraitMois,'depotMois':depotMois,'dateNow':datetime.date(datetime.now()),'M_Now':2}
	return render(request, "Transaction/chart.html",context)