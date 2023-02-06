from .models import Dab

def notification(request):
	billets = Dab.objects.all()
	email = request.session.get("email","Vide")
	prenom = request.session.get("prenom","Vide")
	Numcarte = request.session.get("Numcarte","Vide")
	idDab = request.session.get("idDab","Vide")
	return {"billets" : billets,"prenom":prenom,"email":email,"Numcarte":Numcarte,"idDab":idDab}