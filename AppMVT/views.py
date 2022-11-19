from django.shortcuts import render

# Create your views here.

#importo las clases para poder manejar los templates

from django.template import Template, context, loader

from django.http import HttpResponse

from  .models import Familiar

def familiares(request):

    #Creo los objetos familiar para cada uno de los familiares
    datos_familiar1 ={"id":1,  "nombre":"Susana", "fechaNacimiento":'1957-01-05'}
    datos_familiar2 ={"id":2, "nombre":"Jose Azcarate", "fechaNacimiento":'1950-01-06'}
    datos_familiar3 = {"id":3, "nombre":"Silvia Azcarate", "fechaNacimiento":'1983-01-07'}
       

    familiar1 = Familiar(datos_familiar1['id'], datos_familiar1['nombre'], datos_familiar1['fechaNacimiento'])
    familiar2 = Familiar(datos_familiar2['id'], datos_familiar2['nombre'], datos_familiar2['fechaNacimiento'])
    familiar3 = Familiar(datos_familiar3['id'], datos_familiar3['nombre'], datos_familiar3['fechaNacimiento'])
    
    #los guardo
    familiar1.save()
    familiar2.save()
    familiar3.save()
    diccionario  ={"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3}
    #preparo el template
    plantilla = loader.get_template('template_familia.html')
    
    documento = plantilla.render(diccionario)
    #Mando a renderizar los datos de los familiares

    #documento = plantilla.render(datos_familiar1,datos_familiar2,datos_familiar3)

    
    #muestro en el template

    return HttpResponse(documento)


