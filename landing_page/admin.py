from django.contrib import admin
from django import forms
from landing_page.models import CabLandingPage
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.fields import GenericRelation
from imagen.models import Imagen
from imagen.forms import addImagenForms, ImagenForms
# Register your models here.
class ImagenInline(GenericTabularInline):
    model = Imagen
    form = ImagenForms
    extra = 0
class CabLandingPageAdmin(admin.ModelAdmin):
    inlines = [
        ImagenInline,
    ]
    def save_formset(self, request, form, formset, change):        
        super(CabLandingPageAdmin, self).save_formset(request, form, formset, change)
        instances = formset.save(commit=False)
        print request.FILES
        print instances
        iter1 = 0
        for instance in instances:
            # TENGO QUE ACCEDER al fichero y no iterar sobre todos ellos.
            iter2 = 0
            for fichero in request.FILES:                
                if iter1 == iter2:
                    print 'entro %i' % iter2 
                    instance.file = request.FILES[fichero].read()
                    instance.content_type_file = request.FILES[fichero].content_type
                    print instance.lugar
                    #print request.POST
                    #instance.denominacion = request.FILES[fichero].name
                iter2 = iter2 +1
            iter1 = iter1+1
            instance.save()
        print 'save_formset'
        #print formset
        #print form
    def save_model(self, request, obj, form, change):
        super(CabLandingPageAdmin, self).save_model(request, obj, form, change)
#         print 'save_model'
#         print obj.imagen.instance.imagen.count()
#         # if change se busca obj sino, pues se crea
#         print change
#         #print self
#         #print request.FILES['imagen-imagen-content_type-object_id-0-fich'].read()
#         print obj
#         iter = 0
#         #print obj.imagen.count()
#         obj.save()
#         print 'despues save'
#         print obj.imagen.count()
#         for fichero in request.FILES:
#             print request.FILES[fichero]
#             fich = request.FILES[fichero].read()
#             print request.FILES[fichero].content_type
#             ctf = request.FILES[fichero].content_type
#             if change:
#                 #print obj.imagen.all()[iter].denominacion
#                 #print obj.imagen.all()[iter].denominacion
#                 print 'update'
#                 #obj.imagen.all()[iter].content_type_file = request.FILES[fichero].content_type
#                 obj.imagen.update_or_create(pk=obj.imagen.all()[iter].pk,file=fich,content_type_file = ctf, content_type = obj.imagen.content_type, object_id = obj.pk,denominacion=obj.imagen.all()[iter].denominacion)
#                 #imagen.content_type_file = request.FILES[fichero].content_type
#                 print obj.imagen.values()[iter]
#             else:
#                 print 'add'
#                 obj.save()
#                 print obj.pk
#                 obj.imagen.get_or_create(file=fich,content_type_file = ctf, content_type = obj.imagen.content_type, object_id = obj.pk,denominacion=request.FILES[fichero].name)
#             #print imagen.content_type_file
#                 print 'adios'
#             iter +=1
#         print 'bucle'
#         print obj.imagen.count()
        #super(CabLandingPageAdmin, self).save(request, obj, forms, change)
        #0print obj.imagen.pk_val
        #print obj.imagen.model
        #print obj.imagen.content_type
        #print obj.imagen.symmetrical
        #print obj.imagen.instance
        #print obj.imagen.instance.imagen.get().denominacion
        #obj.imagen.instance.imagen.get().set(denominacion = "claudio")
        #print obj.imagen.instance.imagen.get().denominacion

        #print obj.imagen.source_col_name
        #print obj.imagen.target_col_name
        #print obj.imagen.content_type_field_name
        #print obj.imagen.object_id_field_name
        #print obj.imagen.prefetch_cache_name 
        #print obj.imagen.pk_val
        #print obj.imagen.core_filters
        #print obj.imagen.values()
        #img = obj.imagen
        #print img
        
        
        #img.set(file=request.FILES['imagen-imagen-content_type-object_id-0-fich'].read())
        #print img
        #algo = request.FILES['imagen-imagen-content_type-object_id-0-fich'].read()
        #ct_file = request.FILES['imagen-imagen-content_type-object_id-0-fich'].content_type
        #print ct_file
        #print algo
        #img.set(algo)
        #print gen
        #print 'algo'
        #print img.file
        #img.file = algo
        #img.content_type_file = ct_file
        #print obj.imagen.model
        #print obj.imagen.content_type
        #print img.pk
        #obj.set_imagen(file=algo)
        #aux.file = algo
        #aux.content_type_file = ct_file
        #aux.save()
        
        #obj.imagen.content_type.file = algo
        #default_values = {'file' :algo, 'content_type_file' :ct_file}
        #obj.imagen.update_or_create(file=algo,content_type_file=ct_file)
        #timg = Imagen.objects.filter(pk=img.pk).first()
        #timg.content_type_file = img.content_type_file
        #timg.file = img.file
        #print timg.denominacion
        #timg.denominacion ="full"
        #print timg.denominacion
        #timg.save(force_update=True)
        #timg = Imagen.objects.filter(pk=img.pk).first()
        #print timg.denominacion
        #print timg.pk
        #obj.imagen.add(timg)
        #print obj.imagen.values_list()
        #tak = obj
        #print tak.imagen.values()
        #tak.save(force_update=True)
        #super(CabLandingPageAdmin,self).save_model(request, tak, form, change)
        #print tak.imagen.get().file
        #obj.imagen.update_or_create(imagen=img)
        #print img.file
        #print img.content_type_file
        #obj.imagen = GenericRelation(img)
        #print obj.imagen.get().file
        #print obj.imagen.get().denominacion
        #obj.imagen.get().file = algo
        #obj.imagen.get().content_type_file = ct_file
        #obj.imagen.get().set(file=img.file)
        #print obj.imagen.get().file
        #print obj.imagen.Modify(file=request.FILES['imagen-imagen-content_type-object_id-0-fich'].read())
        #obj.imagen.Modify(file=request.FILES['imagen-imagen-content_type-object_id-0-fich'].read())
        #print form
        #print change
        #admin.ModelAdmin.save_model(self, request, obj, form, change)
        #print obj.imagen.values().count()

    


admin.site.register(CabLandingPage, CabLandingPageAdmin)