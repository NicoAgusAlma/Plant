import random

from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from requests import request
from django.db.models import Q
from BlogPlantas.forms import PosteoFormulario, UserRegisterForm
from django.urls import reverse_lazy
from BlogPlantas.models import ImagenPlanta, Vivero, Planta, Posteo, Problema, Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        form2 = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, 'BlogPlantas/inicio.html', {'mensaje':f', Bienvenido {usuario}'})
            else:
                return render(request, 'BlogPlantas/inicio.html', {'mensaje':', Error, datos incorrectos'})
        elif form2.is_valid:
            try:
                form2.save()
                return render(request=request, 
                template_name='BlogPlantas/inicio.html', 
                context={'mensaje':', Usuario creado'})
            except:
                return render(request, 'BlogPlantas/error_registro.html', {'mensaje':', Error, formulario erroneo'})
        else:
            return render(request, 'BlogPlantas/inicio.html', {'mensaje':', Error, formulario erroneo'})
    form = AuthenticationForm()
    form2=UserRegisterForm()
    return render(request, 'BlogPlantas/login.html', {'form':form, 'form2':form2})

def register(request):
    if request.method =='POST':
        form2 = UserRegisterForm(request.POST)
        if form2.is_valid:
            try:
                form2.save()
                return render(request=request, 
                template_name='BlogPlantas/inicio.html', 
                context={'mensaje':', Usuario creado'})
            except:
                return render(request, 'BlogPlantas/error_registro.html', {'mensaje':', Error, formulario erroneo'})
    form2=UserRegisterForm()
    return render(request=request, 
    template_name='BlogPlantas/registro.html', 
    context={'form':form2})
    
    

# def login_request(request):
#     if request.method == 'POST':
#         form=AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usuario=form.cleaned_data.get('username')
#             contra=form.cleaned_data.get('password')
#             user=authenticate(username=usuario, password=contra)
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'BlogPlantas/inicio.html', {'mensaje':f', Bienvenido {usuario}'})
#             else:
#                 return render(request, 'BlogPlantas/inicio.html', {'mensaje':', Error, datos incorrectos'})
#         else:
#             return render(request, 'BlogPlantas/inicio.html', {'mensaje':', Error, formulario erroneo'})
#     form = AuthenticationForm()
#     return render(request, 'BlogPlantas/login.html', {'form':form})

# def register(request):
#     if request.method =='POST':
#         form2 = UserRegisterForm(request.POST)
#         if form2.is_valid:
#             try:
#                 form2.save()
#                 return render(request=request, 
#                 template_name='BlogPlantas/inicio.html', 
#                 context={'mensaje':', Usuario creado'})
#             except:
#                 return render(request, 'BlogPlantas/error_registro.html', {'mensaje':', Error, formulario erroneo'})
#     form=UserRegisterForm()
#     return render(request=request, 
#     template_name='BlogPlantas/registro.html', 
#     context={'form':form2})


def inicio(request):
    return render(request, 'BlogPlantas/inicio.html')

def contacto(request):
    return render(request, 'BlogPlantas/contacto.html')

def plantas(request):
    return render(request, 'BlogPlantas/plantas.html')

def viveros(request):
    return render(request, 'BlogPlantas/viveros.html')

def viveros_todos(request):
    viveros = Vivero.objects.all()
    contexto={'viveros':viveros}
    return render(request, 'BlogPlantas/viveros_todos.html', contexto)

def buscador(request):
    return render(request, 'BlogPlantas/resultado_busqueda.html',{'search_param':''})

# VIVEROS

class ViveroList(ListView):
    model = Vivero
    template_name = 'BlogPlantas/viveros_list.html'

class ViveroDetail(DetailView):
    model = Vivero
    template_name = 'BlogPlantas/vivero_detalle.html'

class ViveroCreate(LoginRequiredMixin, CreateView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono','stockPlantas','stockProductos', 'imagen']

class ViveroUpdate(LoginRequiredMixin, UpdateView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono','stockPlantas','stockProductos', 'imagen']

class ViveroDelete(LoginRequiredMixin, DeleteView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    
# PLANTAS

class PlantaList(ListView):
    model = Planta
    template_name = 'BlogPlantas/plantas_list.html'
    

class PlantaDetail(DetailView):
    model = Planta
    template_name = 'BlogPlantas/planta_detalle.html' 

class PlantaCreate(LoginRequiredMixin, CreateView):
    model = Planta
    success_url = reverse_lazy('BlogPlantas:ListaPlantas')
    fields = ['nombreComun','nombreCientifico','familia','sustrato','precio','viveros','peligrosComunes','interior','luzDirecta','frecuenciaRiego','descripcion', 'imagen']

class PlantaUpdate(LoginRequiredMixin, UpdateView):
    model = Planta
    success_url = reverse_lazy('BlogPlantas:ListaPlantas')
    fields = ['nombreComun','nombreCientifico','familia','sustrato','precio','viveros','peligrosComunes','interior','luzDirecta','frecuenciaRiego','descripcion']

class PlantaDelete(LoginRequiredMixin, DeleteView):
    model = Planta
    success_url = reverse_lazy('BlogPlantas:ListaPlantas')

# PRODUCTOS

class ProductoList(ListView):
    model = Producto
    template_name = 'BlogPlantas/productos_list.html'

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'BlogPlantas/producto_detalle.html'

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = reverse_lazy('BlogPlantas:ListaProductos')
    fields = ['nombre','precio','solucionaProblemas','puntoDeVenta', 'imagen']

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy('BlogPlantas:ListaProductos')
    fields = ['nombre','precio','solucionaProblemas','puntoDeVenta', 'imagen']

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('BlogPlantas:ListaProductos')

# PROBLEMAS

class ProblemaList(ListView):
    model = Problema
    template_name = 'BlogPlantas/problemas_list.html'

class ProblemaDetail(DetailView):
    model = Problema
    template_name = 'BlogPlantas/problema_detalle.html'

class ProblemaCreate(LoginRequiredMixin, CreateView):
    model = Problema
    success_url = reverse_lazy('BlogPlantas:ListaProblemas')
    fields = ['nombreProblema','nombreCientifico','peligro','productos','solucion', 'imagen']

class ProblemaUpdate(LoginRequiredMixin, UpdateView):
    model = Problema
    success_url = reverse_lazy('BlogPlantas:ListaProblemas')
    fields = ['nombreProblema','nombreCientifico','peligro','productos','solucion', 'imagen']

class ProblemaDelete(LoginRequiredMixin, DeleteView):
    model = Problema
    success_url = reverse_lazy('BlogPlantas:ListaProblemas')

# GALERIA

class Galeria(ListView):
    model = Planta
    template_name = 'BlogPlantas/galeria.html'



# POSTEOS

class PosteoList(ListView):
    model = Posteo
    template_name = 'BlogPlantas/posteos_list.html'
    posteo_titulo = Posteo.objects.all()
    cant_posteos = (Posteo.objects.all()).count()
    id_titulo = {}
    contador=0
    if cant_posteos >= 5:
        post_random=random.sample(range(cant_posteos), 5)
        # for i in post_random:
            # post_random[i]=post_random[i]+1
            # posteo_titulo = Posteo.objects.filter(id=post_random[i])
            # posteo_titulo = posteo_titulo.get(id=post_random[i])
            # id_titulo[post_random[i]]=posteo_titulo

    else:
        post_random=random.sample(range(cant_posteos), cant_posteos)
        print(post_random)
        for i in post_random:
            print(i)
            post_random[contador]=i+1
            contador+=1
        for i in post_random:
            posteo_info = Posteo.objects.filter(id=i)
            print(posteo_info)
            #  titulo = posteo_info.titulo
            id_titulo[i]=posteo_info
            
        print(id_titulo)
    

    print(cant_posteos)
    print(post_random)
    print('HOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    extra_context= {'posteos':posteo_titulo, 'post_random':post_random, 'id_titulo':id_titulo}

class PosteoDetail(DetailView):
    model = Posteo
    template_name = 'BlogPlantas/posteo_detalle.html'

class PosteoCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    success_url = reverse_lazy('BlogPlantas:ListaPosteos')
    fields = ['titulo','subtitulo','fecha','texto','autor', 'imagen']

class PosteoUpdate(LoginRequiredMixin, UpdateView):
    model = Posteo
    success_url = reverse_lazy('BlogPlantas:ListaPosteos')
    fields = ['titulo','subtitulo','fecha','texto','autor', 'imagen']

class PosteoDelete(LoginRequiredMixin, DeleteView):
    model = Posteo
    success_url = reverse_lazy('BlogPlantas:ListaPosteos')

def buscar(request):
    if request.GET['busqueda']:
        search_param = request.GET['busqueda']
        print(search_param)
        query = Q(nombreComun__contains=search_param)
        query.add(Q(nombreCientifico__contains=search_param), Q.OR)
        query.add(Q(familia__contains=search_param), Q.OR)
        query.add(Q(sustrato__contains=search_param), Q.OR)
        query.add(Q(viveros__contains=search_param), Q.OR)
        query.add(Q(peligrosComunes__contains=search_param), Q.OR)
        plantas = Planta.objects.filter(query)
        query = Q(nombreProblema__contains=search_param)
        query.add(Q(nombreCientifico__contains=search_param), Q.OR)
        query.add(Q(peligro__contains=search_param), Q.OR)
        query.add(Q(productos__contains=search_param), Q.OR)
        query.add(Q(solucion__contains=search_param), Q.OR)        
        problemas = Problema.objects.filter(query)
        query = Q(nombre__contains=search_param)
        query.add(Q(provincia__contains=search_param), Q.OR)
        query.add(Q(localidad__contains=search_param), Q.OR)
        query.add(Q(calle__contains=search_param), Q.OR)
        query.add(Q(stockPlantas__contains=search_param), Q.OR)        
        query.add(Q(stockProductos__contains=search_param), Q.OR)        
        viveros = Vivero.objects.filter(query)
        query = Q(nombre__contains=search_param)
        query.add(Q(solucionaProblemas__contains=search_param), Q.OR)
        query.add(Q(puntoDeVenta__contains=search_param), Q.OR)               
        productos = Producto.objects.filter(query)
        query = Q(titulo__contains=search_param)
        query.add(Q(subtitulo__contains=search_param), Q.OR)
        query.add(Q(texto__contains=search_param), Q.OR)               
        query.add(Q(autor__contains=search_param), Q.OR)               
        posteos = Posteo.objects.filter(query)
        context_dict = {
            'search_param':search_param,
            'plantas': plantas,
            'problemas': problemas,
            'viveros':viveros,
            'productos':productos,
            'posteos':posteos
        }
        
        return render(
            request=request,
            context=context_dict,
            template_name="BlogPlantas/resultado_busqueda.html",
        )
    else:

        respuesta = 'No ingresó ningun dato' 

        return render(request, 'BlogPlantas/resultado_busqueda.html', {'respuesta':respuesta})
    



# luego de eso hacer lo mismo para el resto de las clases del modelo
# luego gestionar lo de login, logout, etc
# luego ver lo de las imagenes de cada cosa
# ver menus desplegables para seleccionar viveros
# luego ver como muestra una lista de 10 posteos y mas paginas debajo para recorrer
# chequear los campos booleanos en los html que no aparecen
# luego darle estetica



# def editarPerfil(request):
#     usuario=request.user
#     if request.method=="POST":
#         miFormulario = UserEditForm(request.POST)
#         if miFormulario.is_valid:
#             informacion=miFormulario.cleaned_data
#             usuario.username=informacion['username']
#             usuario.email=informacion['email']
#             usuario.password1=informacion['password1']
#             usuario.password2=informacion['password2']
#             usuario.save()
#             return render(request, "BlogPlantas/usuario_modificado.html")
#     else:
#         miFormulario=UserEditForm(initial={'email':usuario.email})
    
#     return render(request, 'BlogPlantas/edita_perfil.html', {'miFormulario':miFormulario, 'usuario':usuario})

# def posteoFormulario(request):
#     if request.method == 'POST':
#         miFormulario = PosteoFormulario(request.POST)
#         print(miFormulario)
#         if miFormulario.is_valid:
#             informacion = miFormulario.cleaned_data
#             posteo=Posteo(titulo=informacion['titulo'], 
#                 subtitulo=informacion['subtitulo'], 
#                 fecha=informacion['fecha'], 
#                 texto=informacion['texto'],
#                 autor=informacion['autor'],
#                 )
#             posteo.save()
#             return render(request, 'BlogPlantas/posteos_list.html')
#     else:
#         miFormulario = PosteoFormulario()
#     return render(request, 'BlogPlantas/posteo_form.html', {'miFormulario':miFormulario})
