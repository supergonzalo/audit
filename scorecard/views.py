from scorecard.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from scorecard.etiqueta import * 
import os

def lista(request):
	return render_to_response('lista.html', {'current': edificio.objects.all()}) 

def edif(request, edif):
	var=G(edif)
        var['mensaje'] = "Informe"
        var['columna'] = 0
	return render_to_response('edificio.html', var)

def formato(request):
	response = open(os.getcwd() + "/scorecard/templates/negro.png").read()
	return HttpResponse(response)

def home(request):
        mensaje = "Testing de evaluador de performance de edificios. Uso privado."
	columna = "Version de prueba"
        return render_to_response('tagg.html', {'mensaje': mensaje,'columna':columna})

