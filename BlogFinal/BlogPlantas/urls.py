from django.urls import path
from BlogPlantas import views
from django.contrib.auth.views import LogoutView


app_name='BlogPlantas'
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Registro'),
    path('logout', LogoutView.as_view(template_name='BlogPlantas/logout.html'), name='Logout'),
    # path('editar_perfil', views.editarPerfil, name='EditarPerfil'),
    
    # VIVEROS
    path('viveros/list', views.ViveroList.as_view(), name='ListaViveros'),
    path('vivero/add', views.ViveroCreate.as_view(), name='AgregarVivero'),
    path('vivero/<int:pk>/detail', views.ViveroDetail.as_view(), name='DetalleVivero'),
    path('vivero/<int:pk>/update', views.ViveroUpdate.as_view(), name='UpdateVivero'),
    path('vivero/<int:pk>/delete', views.ViveroDelete.as_view(), name='BorrarVivero'),
    
    # PLANTAS
    path('plantas/list', views.PlantaList.as_view(), name='ListaPlantas'),
    path('planta/add', views.PlantaCreate.as_view(), name='AgregarPlanta'),
    path('planta/<int:pk>/detail', views.PlantaDetail.as_view(), name='DetallePlanta'),
    path('planta/<int:pk>/update', views.PlantaUpdate.as_view(), name='UpdatePlanta'),
    path('planta/<int:pk>/delete', views.PlantaDelete.as_view(), name='BorrarPlanta'),
   
    # PRODUCTOS
    path('productos/list', views.ProductoList.as_view(), name='ListaProductos'),
    path('producto/add', views.ProductoCreate.as_view(), name='AgregarProducto'),
    path('producto/<int:pk>/detail', views.ProductoDetail.as_view(), name='DetalleProducto'),
    path('producto/<int:pk>/update', views.ProductoUpdate.as_view(), name='UpdateProducto'),
    path('producto/<int:pk>/delete', views.ProductoDelete.as_view(), name='BorrarProducto'),
   
    # PROBLEMAS
    path('problemas/list', views.ProblemaList.as_view(), name='ListaProblemas'),
    path('problema/add', views.ProblemaCreate.as_view(), name='AgregarProblema'),
    path('problema/<int:pk>/detail', views.ProblemaDetail.as_view(), name='DetalleProblema'),
    path('problema/<int:pk>/update', views.ProblemaUpdate.as_view(), name='UpdateProblema'),
    path('problema/<int:pk>/delete', views.ProblemaDelete.as_view(), name='BorrarProblema'),
   
    # POSTEOS
    path('posteos/list', views.PosteoList.as_view(), name='ListaPosteos'),
    path('posteo/add', views.PosteoCreate.as_view(), name='AgregarPosteo'),
    path('posteo/<int:pk>/detail', views.PosteoDetail.as_view(), name='DetallePosteo'),
    path('posteo/<int:pk>/update', views.PosteoUpdate.as_view(), name='UpdatePosteo'),
    path('posteo/<int:pk>/delete', views.PosteoDelete.as_view(), name='BorrarPosteo'),

    # BUSCADOR
    path('buscar/', views.buscar),
    path('buscador/', views.buscador, name='Buscador'),

    #GALERIA
    path('galeria', views.Galeria.as_view(), name='Galeria'),

    #CONTACTO
    path('contacto', views.contacto, name='Contacto'),
   
]

