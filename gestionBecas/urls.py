from django.urls import path
from . import views 
from .views import lista_usuarios
from .views import inicio_SinRol
from .views import registrar_programa_beca
app_name = 'app_login'

urlpatterns  = [  
  path('inicio/', views.inicio_view, name='inicio'),  
  path('inicio_sesion/', views.login_view, name='login'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.signup_view, name='signup'),
  path('perfil/', views.perfil, name='perfil'),
  path('', views.homepage, name='homepage'),
  path('asignar_roles/', views.asignar_roles, name='asignar_roles'),
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

