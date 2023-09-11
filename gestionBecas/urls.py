from django.urls import path
from . import views 

app_name = 'app_login'

urlpatterns  = [  
     path('inicio/', views.inicio_view, name='inicio'),  
path('inicio_sesion/', views.login_view, name='login'),
 path('login/', views.login_view, name='login'),
]
