from django.db import models

class domicilio(models.Model):
    calle = models.CharField(max_length=100)
    no_calle = models.CharField(max_length=20)
    pais = models.CharField(max_length=10)

    def __str__(self):
        return f'Domicilio{self.id}: {self.calle} {self.no_calle} '

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    edad = models.IntegerField()
    SEXO_CHOICES = (
        ('F','Femenino'),
        ('M','Masculino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    domicilio = models.ForeignKey(domicilio,on_delete=models.SET_NULL,null=True)
# Create your models here.

    def __str__(self):
        return f'Persona{self.id}: {self.nombre} {self.apellido}'

