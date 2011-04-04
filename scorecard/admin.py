from scorecard.models import * 
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *

admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(Group)

class paredAdmin(admin.ModelAdmin):
	list_display=('nombre_edif','nombre_amb','orientacion_pared')
		
class artefactoAdmin(admin.ModelAdmin):
        list_display=('descriptor','nombre_edif','ambiente_artefacto')


class estructuraAdmin(admin.ModelAdmin):

	list_display=('nombre','k')

        def save_model(self,request,obj,form,change):
		obj.k=0.195
		try:
			obj.k+=obj.espesor_pared/obj.pared_externa
		except:
			pass
		try:
			obj.k+=obj.espesor_medio/obj.medio
		except:
			pass
		try:
			obj.k+=obj.espesor_interna/obj.pared_interna
		except:
			pass
		try:
			obj.k+=obj.espesor_revest/obj.revestimiento_interno
		except:
			pass
		obj.k=1/obj.k
		#print "CUENTA: 0.195 + %s+ %s + %s +%s "%(obj.espesor_pared/obj.pared_externa,obj.espesor_medio/obj.medio,obj.espesor_interna/obj.pared_interna,obj.espesor_revest/obj.revestimiento_interno)
		obj.save()
		
class ambienteAdmin(admin.ModelAdmin):
        list_display=('nombre_edif','nombre_amb')








admin.site.register(edificio)
admin.site.register(ambiente,ambienteAdmin)
admin.site.register(artefacto,artefactoAdmin)
admin.site.register(pared,paredAdmin)
admin.site.register(estructura,estructuraAdmin)
admin.site.register(techo)

