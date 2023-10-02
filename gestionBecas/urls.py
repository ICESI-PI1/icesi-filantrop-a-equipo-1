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
]
