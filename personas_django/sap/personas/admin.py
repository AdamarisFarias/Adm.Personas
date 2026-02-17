from django.contrib import admin

# Register your models here.
from personas.models import Persona
from personas.models import Persona, domicilio
admin.site.register(Persona)
admin.site.register(domicilio)
