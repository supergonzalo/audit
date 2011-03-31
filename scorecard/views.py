from scorecard.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from scorecard.etiqueta import * 
import os

def lista(request):
	return render_to_response('lista.html', {'current': edificio.objects.all()}) 

def edif(request, edif):
	return render_to_response('edificio.html', G(edif))

def formato(request,dummy):
	print formato
	response = open(os.getcwd() + "/templates/negro.png").read()
	return HttpResponse(response)
