from . import views
from django.urls import path
from .views.asignar_roles_view import AsignarRolesView
from .views.lista_usuarios_view import ListaUsuariosView
from .views.login_view import LoginView
from .views.inicio_view import InicioView
from .views.signup_view import SignupView
from .views.homepage_view import HomepageView
from .views.informes_estadisticas import InformesyEstadisticas
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
from .views.eliminar_programa_beca import EliminarProgramaBeca, EliminarProgramaBecaIndividual
from .views.obtener_becas import ObtenerProgramasBecaView,DetallesProgramaBecaView


app_name = 'app_login'

urlpatterns  = [  
    path('asignar_roles_view/', views.asignar_roles_view.AsignarRolesView.as_view(), name='asignar_roles_view'),
    path('lista_usuarios/', views.lista_usuarios_view.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('login/', views.login_view.LoginView.as_view(), name='login'),
    path('inicio/', views.inicio_view.InicioView.as_view(), name='inicio'),
    path('signup/', views.signup_view.SignupView.as_view(), name='signup'),
    path('', views.homepage_view.HomepageView.as_view(), name='homepage'),
    path('informes_estadisticas/', views.informes_estadisticas.InformesyEstadisticas.as_view(), name='informes_estadisticas'),
    path('perfil/', views.perfil_view.PerfilView.as_view(), name='perfil'),
    path('gestion_programa_beca/', views.gestion_programa_beca_view.GestionProgramaBecaView.as_view(), name='gestion_programa_beca'),
    path('inicio_sin_rol/', views.inicio_sin_rol_view.InicioSinRolView.as_view(), name='inicio_sin_rol'),
    path('inicio_donante/', views.inicio_donante_view.InicioDonanteView.as_view(), name='inicio_donante'),
    path('ver_programa_beca/', views.ver_programa_beca_view.VerProgramaBecaView.as_view(), name='ver_programa_beca'),
    path('seleccionar_pb2/', views.seleccionar_pb2.Seleccionar2ProgramaBecaView.as_view(), name='seleccionar_pb2'),
    path('seleccionar_programa_beca/', views.seleccionar_programa_beca_view.SeleccionarProgramaBecaView.as_view(), name='seleccionar_programa_beca'),
    path('editar_programa_beca/<int:programa_id>/', views.editar_programa_beca_view.EditarProgramaBecaView.as_view(), name='editar_programa_beca'),
    path('registrar_cronograma/<int:programa_id>/', views.registrar_cronograma_view.CrearCronogramaView.as_view(), name='registrar_cronograma'),
    path('gestion_informe_beca/', views.gestion_informe_beca_view.GestionInformeBecaView.as_view(), name='gestion_informe_beca'),
    path('seleccionar_cronograma/', views.seleccionar_cronograma_view.SeleccionarCronogramaView.as_view(), name='seleccionar_cronograma'),
    path('editar_cronograma/<int:cronograma_id>/', views.editar_cronograma_view.EditarCronogramaView.as_view(), name='editar_cronograma'),
    path('registrar_programa_beca/', views.registrar_programa_beca_view.RegistrarProgramaBecaView.as_view(), name='registrar_programa_beca'),
    path('eliminar_usuario/<str:username>/', views.eliminar_usuario_view.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('editar_roll/<str:username>/', views.editar_roll_view.EditarRollNameView.as_view(), name='editar_rollname'),
    path('eliminar_cronograma/', views.eliminar_cronograma.EliminarCronograma.as_view(), name='eliminar_cronograma'),
   path('eliminar_cronograma_individual/<int:cronograma_id>/', views.eliminar_cronograma.EliminarCronogramaIndividual.as_view(), name='eliminar_cronograma_individual'),
    path('ver_cronograma/', views.ver_cronograma.VerCronogramaView.as_view(), name='ver_cronograma'),
    path('eliminar_programa_beca/', views.eliminar_programa_beca.EliminarProgramaBeca.as_view(), name='eliminar_programa_beca'),
   path('eliminar_programa_beca_individual/<int:programa_id>/', views.eliminar_programa_beca.EliminarProgramaBecaIndividual.as_view(), name='eliminar_programa_beca_individual'),
    path('obtener_becas/', views.obtener_becas.ObtenerProgramasBecaView.as_view(), name='obtener_beca'),
     path('obtener_detalles_programa_beca/<int:id_programa_beca>/', views.obtener_becas.DetallesProgramaBecaView.as_view(), name='obtener_detalles_programa_beca'),
    
]
