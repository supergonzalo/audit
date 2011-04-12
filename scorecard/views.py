from scorecard.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from scorecard.etiqueta import * 
import os

def lista(request):
	return render_to_response('lista.html', {'current': edificio.objects.all()}) 

def edif(request, edif):
	var=G(edif)
        var['mensaje'] = "Testing de evaluacion de performance de edificios. Uso privado."
        var['columna'] = ""
	var['equipos']=wattage(edif)
	return render_to_response('edificio.html', var)

def formato(request):
	response = open(os.getcwd() + "/scorecard/templates/negro.png").read()
	return HttpResponse(response)

def home(request):
        mensaje = "Testing de evaluacion de performance de edificios. Uso privado."
	obj="Objetivos"
	body="Mediante la construccion de un modelo simulado del sistema edificio+equipos+usuarios proyectar el consumo energetico teorico y contrastarlo contra valores medidos. Dimensionar intalaciones y equipos, evaluar estrategias para optimizar el consumo energetico, proyectar ahorro."
	columna = "Version de prueba"
        return render_to_response('tagg.html', {'mensaje': mensaje,'columna':columna,'obj':obj,'body':body})

