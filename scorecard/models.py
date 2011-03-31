from django.db import models
import pickle

f=open('./scorecard/matlist.pickle','r')
mat=pickle.load(f)
f=open('./scorecard/loc_choices.pickle','r')
localidad_choices=pickle.load(f)


class edificio(models.Model):
	aislacion_choices=((u'Sin aislacion',u'Sin aislacion'),(u'Aislacion perimetral',u'Aislacion perimetral'),(u'Aislacion total',u'Aislacion total')) 
        nombre_edif=models.CharField(max_length=30)
        direccion=models.CharField(max_length=30, null=True)
	localidad=models.CharField(max_length=30,choices=localidad_choices)
        temperatura_aa=models.PositiveSmallIntegerField(choices=((18,18),(20,20),(22,22)))
	perimetro_planta=models.FloatField()
	superficie_planta=models.FloatField()
	aislacion_planta=models.CharField(max_length=30,choices=aislacion_choices)
	plantas=models.PositiveSmallIntegerField()
	recambios_de_aire=models.PositiveSmallIntegerField()
        hora_inicio_semana=models.TimeField()
        hora_fin_semana=models.TimeField()
        hora_inicio_sabado=models.TimeField(blank=True, null=True)
        hora_fin=models.TimeField(blank=True, null=True)
        hora_inicio_domingo=models.TimeField(blank=True, null=True)
        hora_fin_domingo=models.TimeField(blank=True, null=True)

        def __unicode__(self):
                return self.nombre_edif

class ambiente(models.Model):
        tipo_amb_choices=((u'O',u'Oficina'),(u'D',u'Datacenter'),(u'P',u'Pasillo'),(u'R',u'Recepcion'),(u'C',u'Cocina'),(u'S',u'Sala'),(u'd',u'Deposito'))
        nombre_edif=models.ForeignKey(edificio)
        nombre_amb=models.CharField(max_length=30)                              #nombre del ambiente, descriptivo
        cantidad=models.PositiveSmallIntegerField()                                 #piso en el que se encuentra el ambiente
        tipo_amb=models.CharField(max_length=10,choices=tipo_amb_choices)       #tipo de ambiente
        largo_ambiente=models.FloatField()
        ancho_ambiente=models.FloatField()
        altura_techo=models.FloatField()
        personal_permanente=models.PositiveSmallIntegerField(blank=True, null=True)
        def __unicode__(self):
                return self.nombre_amb

class artefacto(models.Model):
        tipo_artefacto_choices=((u'Bajo consumo',u'Bajo consumo'),(u'Tubo de luz',u'Tubo de luz'),(u'Dicroica',u'Dicroica'),(u'Incandescente','Incandescente'),(u'Computadora',u'Computadora'),(u'Impresora',u'Impresora'),(u'Proyector',u'Proyector'),(u'Heladera',u'Heladera'),(u'Cocina electrica',u'Cocina electrica'),(u'Estufa electrica',u'Estufa electrica'),(u'Otro',u'Otro'))
        descriptor=models.CharField(max_length=20,blank=True, null=True)
        ciclo_activo_choices=((u'E',u'Siempre activo'),(u'L',u'Activo horario laboral'),(u'O',u'Activo 50% horario laboral'),(u'N',u'Activo horario NO laboral'))
        nombre_edif=models.ForeignKey(edificio)
        ambiente_artefacto=models.ForeignKey(ambiente)
        tipo_artefacto=models.CharField(max_length=20,choices=tipo_artefacto_choices)
        potencia_activo=models.FloatField()
        potencia_stand_by=models.FloatField(blank=True, null=True)
        ciclo_activo=models.CharField(max_length=1,choices=ciclo_activo_choices)
        temp_funcionamiento=models.FloatField(blank=True, null=True)
        cantidad=models.PositiveSmallIntegerField()
        def __unicode__(self):
                return self.tipo_artefacto

class estructura(models.Model):

	mat_choices=mat	
	nombre=models.CharField(max_length=30)
	pared_externa=models.FloatField(choices=mat_choices,blank=True, null=True)
	espesor_pared=models.FloatField(blank=True, null=True)
	medio=models.FloatField(choices=mat_choices,blank=True, null=True)
	espesor_medio=models.FloatField(blank=True, null=True)
	pared_interna=models.FloatField(choices=mat_choices,blank=True, null=True)
	espesor_interna=models.FloatField(blank=True, null=True)
	revestimiento_interno=models.FloatField(choices=mat_choices,blank=True, null=True)
	espesor_revest=models.FloatField(blank=True, null=True)
	k=models.FloatField(blank=True, null=True)
        def __unicode__(self):
                return self.nombre


class pared(models.Model):
        orientacion_choices=((u'Todas',u'Todas(4)'),(u'Norte',u'Norte'),(u'Sur',u'Sur'),(u'Este',u'Este'),(u'Oeste',u'Oeste'))
        exterior_choices=((u'A',u'Opaco Exterior'),(u'B',u'No Opaco Exterior'),(u'I',u'Interior'))

        nombre_edif=models.ForeignKey(edificio)
        nombre_amb=models.ForeignKey(ambiente)
        cantidad=models.PositiveSmallIntegerField()
        orientacion_pared=models.CharField(max_length=6,choices=orientacion_choices)
        area_pared=models.FloatField()
        tipo_de_pared=models.ForeignKey(estructura)
        tipo_de_cerramiento=models.CharField(max_length=1,choices=exterior_choices)
        def __unicode__(self):
                return u'%s %s' % (self.orientacion_pared, self.nombre_amb)


class techo(models.Model):

        nombre_edif=models.ForeignKey(edificio)
        area_techo=models.FloatField()
        tipo_de_techo=models.ForeignKey(estructura)
        def __unicode__(self):
                return u'%s %s' % (self.nombre_edif, self.tipo_de_techo)



