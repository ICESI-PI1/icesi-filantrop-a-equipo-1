from . import views
from django.urls import path
from .views.asignar_roles_view import AsignarRolesView
from .views.lista_usuarios_view import ListaUsuariosView
from .views.login_view import LoginView
from .views.inicio_view import InicioView
from .views.signup_view import SignupView
from .views.homepage_view import HomepageView
from .views.perfil_view import PerfilView
from .views.gestion_programa_beca_view import GestionProgramaBecaView
from .views.inicio_sin_rol_view import InicioSinRolView
from .views.inicio_donante_view import InicioDonanteView
from .views.ver_programa_beca_view import VerProgramaBecaView
from .views.seleccionar_programa_beca_view import SeleccionarProgramaBecaView
from .views.editar_programa_beca_view import EditarProgramaBecaView
from .views.registrar_cronograma_view import CrearCronogramaView
from .views.gestion_informe_beca_view import GestionInformeBecaView
from .views.seleccionar_cronograma_view import SeleccionarCronogramaView
from .views.editar_cronograma_view import EditarCronogramaView
from .views.registrar_programa_beca_view import RegistrarProgramaBecaView
from .views.eliminar_usuario_view import EliminarUsuarioView
from .views.editar_roll_view import EditarRollNameView
from .views.seleccionar_pb2 import Seleccionar2ProgramaBecaView
from .views.eliminar_cronograma import EliminarCronograma, EliminarCronogramaIndividual
from .views.ver_cronograma import VerCronogramaView 

app_name = 'app_login'

urlpatterns  = [  
  path('inicio/', views.inicio_view, name='inicio'),  
  path('inicio_sesion/', views.login_view, name='login'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.signup_view, name='signup'),
  path('perfil/', views.perfil, name='perfil'),
  path('', views.homepage, name='homepage'),
  path('gestion_programa_beca/', views.gestion_programa_beca, name='gestion_programa_beca'),
  path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
  path('editar_firstname/<str:username>/', views.editar_firstname, name='editar_firstname'),
  path('inicio_sin_rol/', inicio_SinRol, name='inicio_sin_rol'),
  path('donante/', views.donante, name='donante'),
  path('eliminar_usuario/<str:username>/', views.eliminar_usuario, name='eliminar_usuario'),
  path('editar_programa_beca/', views.editar_programa_beca, name='editar_programa_beca'),
  path('editar_beca/<int:id_beca>/',views.editar_beca, name='editar_beca'),
  path('ver_programa_beca/', views.ver_programa_beca, name='ver_programa_beca'),
  path('registrar_programa_beca/', views.registrar_programa_beca, name='registrar_programa_beca'),
  path('eliminar_programa_beca/', views.eliminar_programa_beca, name='eliminar_programa_beca'),
  path('eliminar_programa_beca/<str:programa_nombre>/', views.eliminar_programa_beca_individual, name='eliminar_programa_beca_individual'),
  path('ver_programa_beca/', views.ver_programa_beca, name='ver_programa_beca'),

]

