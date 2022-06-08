from email.policy import default
from tkinter import Label
from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ViveroForm(forms.Form):
    nombre=forms.CharField(max_length=40, min_length=3, label='Nombre')
    provincia=forms.CharField(max_length=40)
    localidad=forms.CharField(max_length=40)
    calle=forms.CharField(max_length=40)
    altura=forms.CharField(max_length=40)
    telefono=forms.IntegerField()
    stockPlantas=forms.CharField(help_text='Plantas en stock.', max_length=2000, required=False)
    stockProductos=forms.CharField(help_text='Productos en stock.', max_length=2000, required=False)

class PlantaForm(forms.Form):
    nombreComun=forms.CharField(max_length=40)
    nombreCientifico=forms.CharField(max_length=50, required=False)
    familia=forms.CharField(help_text='Arbol, planta, flor, cactacea, etc.', max_length=50, required=False)
    sustrato=forms.CharField(help_text='Algun tipo de tierra especial?', max_length=50, required=False)
    precio=forms.IntegerField(help_text='Precio en U$s blue.', required=False)
    viveros=forms.CharField(help_text='Viveros donde encontrarla.', required=False, max_length=100)
    peligrosComunes=forms.CharField(help_text='Problemas más usuales.', required=False, max_length=100)
    interior=forms.BooleanField(help_text='La planta es de interior?.', required=False)
    luzDirecta=forms.BooleanField(help_text='Necesita luz solar directa?.', required=False)
    frecuenciaRiego=forms.IntegerField(help_text='Riegos mensuales.', required=False)
    descripcion=forms.CharField(help_text='Descripcion de la planta.', max_length=3000)

class Problema(forms.Form):
    nombreProblema=forms.CharField(max_length=40)
    nombreCientifico=forms.CharField(max_length=50, required=False)
    peligro=forms.CharField(help_text='Bajo, Medio o Alto', max_length=10)
    productos=forms.CharField(help_text='Productos de ayuda.', max_length=50, required=False)
    solucion=forms.CharField(help_text='Manera de solucionarlo', max_length=2000)

class Producto(forms.Form):
    nombre=forms.CharField(max_length=40)
    precio=forms.IntegerField(help_text='Precio en U$s blue.')
    solucionaProblemas=forms.CharField(help_text='Problemas que soluciona.', max_length=200)
    puntoDeVenta=forms.CharField(help_text='Viveros donde comprarlo.', max_length=200)

class PosteoFormulario(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    fecha=forms.DateField(help_text='AAAA/MM/DD')
    texto=forms.CharField(max_length=5000)
    autor=forms.CharField(max_length=100)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password: forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text="Contraloca")
    password1: forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['password1'].label = 'Contraseña'
            self.fields['password2'].label = 'Repetir contraseña'
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','last_name','email','password1','password2']
        help_texts = {k:'' for k in fields}



# class UserEditForm(UserCreationForm):
#     username=forms.CharField(label='Modificar nombre de usuario')
#     email=forms.EmailField(label='Modificar eMail')
#     password1:forms.CharField(label='Contraseña')
#     password2:forms.CharField(label='Repetir contraseña')

#     class Meta:
#         model=User
#         field=['username','email','password1','password2']
#         help_texts={k:'' for k in field}