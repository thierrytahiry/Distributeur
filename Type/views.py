from django.shortcuts import render,redirect
from .forms import TypeForm
from .models import Type

def Type_list(request):
	context = {'type_list': Type.objects.all()}
	return render(request, "Type/type_list.html",context)


def Type_form(request, id=0):
	if request.method =="GET":
		if id == 0:
			form = TypeForm()
		else:
			type = Type.objects.get(pk = id)
			form = TypeForm(instance = type)
		return render(request, "Type/type_form.html", {'form':form})
	else:
		if id == 0:
			form = TypeForm(request.POST)
		else:
			type = Type.objects.get(pk = id)
			form = TypeForm(request.POST,instance = type)
		if form.is_valid():
			form.save()
		return redirect('/Type/listType')

def Type_delete(request, id):
	type = Type.objects.get(pk = id)
	type.delete()
	return redirect('/Type/listType')