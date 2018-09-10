from django.contrib.contenttypes.models import ContentType
from appcc.models import APPCC,ManualAutoControl, PlanAutoControl, CabRegistros,\
    DetallesRegistros, Registros, CuadrosGestion, RelacionesEntes,\
    GestorIncidencias, CabAnaliticas, DetAnaliticas, CabInformesTecnicos,\
    DetInformesTecnicos

def comprobar_autorizacion_reportes(modelo,idmodelo,empresa_id):
    print 'entre a la comprobacion'
    print empresa_id
    print idmodelo
    maestros_generales = ContentType.objects.filter(app_label='maestros')
    
    for maestros in maestros_generales:
        if maestros.model == modelo:
            model = maestros.model_class()
            objeto = model.objects.get(pk=idmodelo)
            if objeto.empresa.pk == empresa_id:
                return True
            
     
    if modelo == 'appcc':
        appcc = APPCC.objects.get(pk=idmodelo)
        emp_id = appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
         
    elif modelo == 'manualautocontrol':
        manautctrl = ManualAutoControl.objects.get(pk=idmodelo)
        emp_id = manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'planautocontrol':
        planautctrl = PlanAutoControl.objects.get(pk=idmodelo)
        emp_id = planautctrl.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'cabregistros':
        cabreg = CabRegistros.objects.get(pk=idmodelo)
        emp_id = cabreg.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'detallesregistros':
        detreg = DetallesRegistros.objects.get(pk=idmodelo)
        emp_id = detreg.cabreg.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'registros':
        reg = Registros.objects.get(pk=idmodelo)
        emp_id = reg.detreg.cabreg.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'cuadrosgestion':
        cuadgest = CuadrosGestion.objects.get(pk=idmodelo)
        emp_id = cuadgest.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'relacionesentes':
        relentes = RelacionesEntes.objects.get(pk=idmodelo)
        emp_id = relentes.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'gestorincidencias':
        gestinc = GestorIncidencias.objects.get(pk=idmodelo)
        emp_id = gestinc.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False 
    elif modelo == 'cabanaliticas':
        cabanalitica = CabAnaliticas.objects.get(pk=idmodelo)
        emp_id = cabanalitica.cabreg.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'detanaliticas':
        detanalitica = DetAnaliticas.objects.get(pk=idmodelo)
        emp_id = detanalitica.cabanalitica.cabreg.manautctrl.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
         
    elif modelo == 'cabinformestecnicos':
        cabifortec = CabInformesTecnicos.objects.get(pk=idmodelo)
        emp_id = cabifortec.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False
    elif modelo == 'detinformestecnicos':
        detifortec = DetInformesTecnicos.objects.get(pk=idmodelo)
        emp_id = detifortec.cabifortec.appcc.empresa.pk
        if emp_id == empresa_id:
            return True
        else:
            return False     