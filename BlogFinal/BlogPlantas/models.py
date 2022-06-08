# from typing_extensions import Required
from email.mime import image
from os import urandom
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Planta(models.Model):
    nombreComun=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)
    familia=models.CharField(help_text='Arbol, planta, flor, cactacea, etc.', max_length=50)
    sustrato=models.CharField(help_text='Algun tipo de tierra especial?', max_length=50)
    precio=models.IntegerField(help_text='Precio en U$s blue.')
    viveros=models.CharField(help_text='Viveros donde encontrarla.', max_length=100)
    peligrosComunes=models.CharField(help_text='Problemas más usuales.', max_length=100)
    interior=models.BooleanField('interior', default=True)
    luzDirecta=models.BooleanField(default=False, help_text='Necesita luz solar directa?.')
    frecuenciaRiego=models.IntegerField(help_text='Riegos mensuales.')
    descripcion=models.CharField(help_text='Descripcion de la planta.', max_length=3000)
    
    def __str__(self):
        return f'{self.nombreComun} / {self.nombreCientifico}'

class ImagenPlanta(models.Model):
    planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)

    def __str__(self):
        return f"{self.imagen.url}"

class Problema(models.Model):
    nombreProblema=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesProblemas', null=True, blank=True)
    peligro=models.CharField(help_text='Bajo, Medio o Alto', max_length=10)
    productos=models.CharField(help_text='Productos de ayuda.', max_length=50)
    solucion=models.CharField(help_text='Manera de solucionarlo', max_length=2000)

    def __str__(self):
        return f'{self.nombreProblema} / {self.nombreCientifico}'

class Vivero(models.Model):
    nombre=models.CharField(max_length=40)
    provincia=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenesViveros', null=True, blank=True)
    localidad=models.CharField(max_length=40)
    calle=models.CharField(max_length=40)
    altura=models.CharField(max_length=40)
    telefono=models.IntegerField()
    stockPlantas=models.CharField(max_length=2000)
    stockProductos=models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.nombre} en {self.localidad}'

class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField(help_text='Precio en U$s blue.')
    imagen=models.ImageField(upload_to='imagenesProductos', null=True, blank=True)
    solucionaProblemas=models.CharField(help_text='Problemas que soluciona.', max_length=200)
    puntoDeVenta=models.CharField(help_text='Viveros donde comprarlo.', max_length=200)

    def __str__(self):
        return f'{self.nombre}'

class Posteo(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField(help_text='AAAA/MM/DD')
    texto=models.CharField(max_length=5000)
    autor=models.CharField(max_length=100, default='Anonimo')
    imagen=models.ImageField(upload_to='imagenesPosteos', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} / {self.fecha} / {self.autor}'
