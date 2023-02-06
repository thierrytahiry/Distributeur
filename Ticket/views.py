from django.shortcuts import render,redirect
from .forms import TicketForm
from .models import Ticket

def Ticket_list(request):
	context = {'ticket_list': Ticket.objects.all()}
	return render(request, "Ticket/ticket_list.html",context)


def Ticket_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = TicketForm()
		else:
			ticket = Ticket.objects.get(pk = id)
			form = TicketForm(instance = ticket)
		return render(request, "Ticket/ticket_form.html", {'form':form})
	else:
		if id == 0:
			form = TicketForm(request.POST)
		else:
			ticket = Ticket.objects.get(pk = id)
			form = TicketForm(request.POST,instance = ticket)
		if form.is_valid():
			form.save()
		return redirect('/Transaction/pageChoix/')

def Ticket_delete(request, id):
	ticket = Ticket.objects.get(pk = id)
	ticket.delete()
	return redirect('/Ticket/listTicket')
