from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from personas.models import Persona

def detallePersona (request,id): #leer unitario
    persona = Persona.objects.get(pk=id)
    return render(request,'personas/detalle.html',{'info_persona':persona})


PersonaForm = modelform_factory(Persona,exclude=[])

def nuevaPersona (request): #creacion de objetos
    if request.method == 'POST':# fase 2, validacion de formulario lleno
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')

        else:
            return render(request,'personas/nuevo.html',{'formulario':formaPersona})

    else:# fase 1, solicitud de formulario vacio
        formaPersona = PersonaForm()
        return render(request,'personas/nuevo.html',{'formulario':formaPersona})


def editarPersona(request,id):
    if request.method == "POST": #fase 2, validamos formulario con informacion editada
        persona = get_object_or_404(Persona,pk=id)
        formaPersona = PersonaForm(request.POST,instance=persona) #formulario lleno con lo que habia + lo que el user cambio
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')

        else:
            return render(request,'personas/editar.html', {'formulario': formaPersona})

    else: #fase 1, se pide formulario lleno con la info de la BD
        persona = get_object_or_404(Persona,pk=id)
        formaPersona = PersonaForm(instance=persona)
        return render(request,'personas/editar.html', {'formulario': formaPersona})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona

def eliminarPersona(request, id):
    if request.method == "POST":  # fase 2: confirmar eliminación
        persona = get_object_or_404(Persona, pk=id)
        persona.delete()
        return redirect('inicio')

    else:  # fase 1: mostrar confirmación
        persona = get_object_or_404(Persona, pk=id)
        return render(request, 'personas/eliminar.html', {'persona': persona})