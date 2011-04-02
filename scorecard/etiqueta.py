from models import *

############################################### Auxiliares #####################################
import bisect

#Tabla de valores de G en funcion de grados dia y superficie
gd=[900,1000,1100,1200,1300,1400,1500,2000,2500,3000,4000,5000]
volumen=[50,100,200,300,400,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,7500,10000]
gadm={
50:[2.713,2.661,2.686,2.560,2.530,2.493,2.469,2.457,2.409,2.353,2.287,2.118],
100:[2.213,2.173,2.133,2.099,2.077,2.050,2.032,2.022,1.986,1.942,1.893,1.762],
200:[1.860,1.828,1.798,1.773,1.757,1.737,1.723,1.715,1.687,1.652,1.613,1.510],
300:[1.704,1.676,1.650,1.629,1.615,1.598,1.587,1.579,1.554,1.523,1.490,1.399],
400:[1.610,1.585,1.562,1.543,1.531,1.516,1.505,1.498,1.475,1.446,1.416,1.322],
500:[1.547,1.523,1.502,1.485,1.473,1.459,1.449,1.443,1.421,1.394,1.366,1.287],
1000:[1.389,1.368,1.352,1.339,1.330,1.319,1.311,1.306,1.287,1.264,1.241,1.174],
1500:[1.319,1.300,1.286,1.274,1.266,1.257,1.250,1.245,1.288,1.206,1.185,1.124],
2000:[1.277,1.259,1.246,1.236,1.228,1.220,1.213,1.208,1.191,1.172,1.152,1.094],
2500:[1.249,1.232,1.219,1.210,1.203,1.195,1.188,1.184,1.169,1.149,1.130,1.074],
3000:[1.228,1.211,1.199,1.190,1.184,1.175,1.170,1.165,1.151,1.131,1.113,1.059],
3500:[1.211,1.195,1.184,1.175,1.169,1.162,1.156,1.151,1.137,1.118,1.100,1.048],
4000:[1.198,1.182,1.171,1.163,1.157,1.150,1.144,1.140,1.126,1.107,1.090,1.038],
4500:[1.187,1.172,1.161,1.153,1.147,1.140,1.135,1.130,1.117,1.098,1.081,1.030],
5000:[1.178,1.163,1.152,1.145,1.139,1.130,1.127,1.122,1.109,1.091,1.074,1.024],
7500:[1.147,1.132,1.123,1.116,1.110,1.104,1.099,1.095,1.082,1.065,1.049,1.002],
10000:[1.128,1.114,1.105,1.099,1.093,1.088,1.083,1.079,1.067,1.050,1.035,0.988]
}

f=open('./scorecard/weather.pickle')
weather=pickle.load(f)

paislacion={'Sin aislacion':{1:1.28,2:1.28,3:1.38,4:1.38,5:1.48,6:1.48},'Aislacion perimetral':{1:1,2:1,3:1.08,4:1.08,5:1.17,6:1.17},'Aislacion total':{1:0.85,2:0.85,3:0.93,4:0.93,5:1,6:1}}
##############################################################################


def gdia(tconfort,localidad):
	return int(weather[localidad]['invierno']['GD'+str(tconfort)])

def lookup_G(vol,gdia):
	return gadm[volumen[bisect.bisect_left(volumen,vol)]][bisect.bisect_left(gd,gdia)]

def pp(iso,zbio):
	return paislacion[iso][int(zbio)] 

#################################################### End of Auxiliares #######################################

def Gadm(edif,volume): #G maximo para una localidad y edificio
	gd_cal=gdia(edif.temperatura_aa,edif.localidad)
	return lookup_G(volume,gd_cal)

def G(edif): # G real del edificio
        build=edificio.objects.get(nombre_edif=edif)
        ambientes=ambiente.objects.filter(nombre_edif=build.pk)
        paredes=pared.objects.filter(nombre_edif=build)
	volume=0.0
        for amb in ambientes:
                volume+=amb.largo_ambiente*amb.ancho_ambiente*amb.altura_techo*amb.cantidad
        gd_cal=gdia(build.temperatura_aa,build.localidad)
	var=dict()
        var['current']=edif
        var['envolvente']=0
        var['sp']=build.superficie_planta
        var['pl']=build.plantas
        var['Gadm']=Gadm(build,volume)
	var['volumen']=volume
	temp=dict()
	try:
        	opacos=paredes.exclude(tipo_de_cerramiento='I').exclude(tipo_de_cerramiento='B')
        	for cada in opacos:
                	est=estructura.objects.filter(nombre=cada.tipo_de_pared)
                	if cada.orientacion_pared=='Todas':
                        	cantidad=4*cada.cantidad
                	else:
                        	cantidad=1*cada.cantidad
                	temp[cada]={'name':est[0].nombre+", "+str(cada.nombre_amb),'sup':cada.area_pared*cantidad,'k':est[0].k,'env':cada.area_pared*est[0].k*cantidad}
		        var['envolvente']+=cada.area_pared*cada.cantidad*est[0].k
        	var['opacos']=temp
	except:
		pass
	temp=dict()
	try:
                noopacos=paredes.exclude(tipo_de_cerramiento='I').exclude(tipo_de_cerramiento='A')
        	for cada in noopacos:
                	if cada.orientacion_pared=='Todas':
                        	cantidad=4*cada.cantidad
                	else:
                        	cantidad=1*cada.cantidad
	                est=estructura.objects.filter(nombre=cada.tipo_de_pared)
        	        temp[cada]={'name':est[0].nombre+", "+str(cada.nombre_amb),'sup':cada.area_pared*cantidad,'k':est[0].k,'env':cada.area_pared*est[0].k*cantidad}
                        var['envolvente']+=cada.area_pared*cada.cantidad*est[0].k
		var['noopacos']=temp
	except:
		pass
        var['n']=build.recambios_de_aire
	var['perdidan']=var['n']*0.35
        var['perim']=build.perimetro_planta
        var['pp']=pp(build.aislacion_planta,weather[build.localidad]['generales']['ZBIO'])
        var['perdida']=var['perim']*var['pp']
        var['ptransm']=var['perdida']+var['envolvente']
        var['pvtransm']=var['ptransm']/var['volumen']
        var['Gsuma']=var['pvtransm']+0.35
	return var

