from idlelib.rpc import request_queue

from django.shortcuts import render
from django.http import HttpResponse

from personas.models import Persona


def bienvenido(request):
    return HttpResponse("Bienvenido")
def contacto(request):
    return HttpResponse("Contacto")
def despedida(request):
    return HttpResponse("Despedida")

# Create your views here.
def bienvenido(request):
    #mensajes = {'msg1' :'Valor mensaje 1', 'msg2' :'Valor mensaje 2', 'msg3' :'Valor mensaje 3'}
    #return render(request,'bienvenido.html', mensajes)
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'Bienvenido.html', {'no_personas':no_personas, 'lista_personas':personas})

