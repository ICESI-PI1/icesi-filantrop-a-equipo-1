from django.urls import path
from . import views 
from .views import lista_usuarios
from .views import inicio_SinRol
app_name = 'app_login'

urlpatterns  = [  
     path('inicio/', views.inicio_view, name='inicio'),  
path('inicio_sesion/', views.login_view, name='login'),
 path('login/', views.login_view, name='login'),
 path('signup/', views.signup_view, name='signup'),
 path('perfil/', views.perfil, name='perfil'),
  path('', views.homepage, name='homepage'),
  path('asignar_roles/', views.asignar_roles, name='asignar_roles'),
  path('gestion_programa_beca/', views.gestion_programa_beca, name='gestion_programa_beca')
  path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
  path('editar_firstname/<str:username>/', views.editar_firstname, name='editar_firstname'),
  path('inicio_sin_rol/', inicio_SinRol, name='inicio_sin_rol'),
  path('inicio_donante/', views.inicio_Donante, name='inicio_donante'),
]
