from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Rol, ProgramaBeca
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import ProgramaBeca
from gestionBecas.forms import ProgramaBecaForm
from .models import ProgramaBeca,TipoConvocatoria, Cronograma

def registrar_programa_beca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaInicio = request.POST.get('fechaInicio')
        fechaFin = request.POST.get('fechaFin')
        cupo = request.POST.get('cupo')
        donantes = request.POST.getlist('donantesSeleccionados')  # Obtener lista de donantes seleccionados
        coberturaEconomica = request.POST.get('coberturaEconomica')
        tipoBeca = request.POST.get('tipoBeca')
        requisitos = request.POST.get('requisitos')

        programa_beca = ProgramaBeca(
            nombre=nombre,
            descripcion=descripcion,
            fechaInicio=fechaInicio,
            fechaFin=fechaFin,
            cupo=cupo,
            donantes=', '.join(donantes),  # Convertir lista de donantes a string
            coberturaEconomica=coberturaEconomica,
            tipoBeca=tipoBeca,
            requisitos=requisitos
        )

        programa_beca.save()  # Guardar el programa de beca en la base de datos

        return render(request, 'registrar_programa_beca.html', {'success_message': 'Programa de Beca registrado exitosamente.'})
    else:
        # Obtener la lista de usuarios
        usuarios = User.objects.filter(first_name='Donante')
        context = {'usuarios': usuarios}
        return render(request, 'registrar_programa_beca.html', context)


def eliminar_usuario(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    return HttpResponse(status=200)

def editar_firstname(request, username):
    usuario = get_object_or_404(User, username=username)

    if request.method == 'POST':
        nuevo_first_name = request.POST.get('first_name')
        if nuevo_first_name:
            usuario.first_name = nuevo_first_name
            usuario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'El campo first_name no puede estar vacío.'})

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)





def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'asignar_roles.html', {'usuarios': usuarios})


def asignar_roles(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        rol_id = request.POST.get('rol')
        
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            rol = Rol.objects.get(id=rol_id)
            
            # Asignar el rol al usuario (dependiendo de cómo esté diseñado tu modelo de datos)
            usuario.roles.add(rol)
            
            return redirect('asignar_roles')
        except Usuario.DoesNotExist or Rol.DoesNotExist:
            # Manejar errores aquí si es necesario
            pass
    
    usuarios = Usuario.objects.all()
    roles = Rol.objects.all()
    
    return render(request, 'asignar_roles.html', {'usuarios': usuarios, 'roles': roles})

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario ha iniciado sesión correctamente
            first_name = user.first_name  
            login(request, user)
            
            #return redirect('app_login:inicio') 
            if first_name == "Sin Rol":
                return redirect('app_login:inicio_sin_rol')  # Reemplaza 'ruta_pagina_uno' con la URL de tu primera página.
            elif first_name == "Administrador":
                return redirect('app_login:inicio')
            elif first_name == "Donante":
                return redirect('app_login:inicio_donante')
            elif first_name == "Filantropia":
                return redirect('app_login:inicio')
            elif first_name == "Beneficiario":
                return redirect('app_login:inicio')
            
            
        else:
            # El inicio de sesión ha fallado, puedes mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    else :
        return render(request, 'login.html') # Redirige a la URL con nombre 'inicio' en la aplicación 'app_login'


def inicio_view(request):

    return render(request, 'inicio.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app_login:login')  # Redirige a la página principal después del registro
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def perfil(request):
    return render(request, 'perfil.html') 

def gestion_programa_beca(request):
    return render(request, 'gestion_programa_beca.html')
def inicio_SinRol(request):
        return render(request, 'inicio_SinRol.html')
    
def inicio_Donante(request):
        return render(request, 'inicio_Donante.html')

def ver_programa_beca(request):
    programas = ProgramaBeca.objects.all()  # Obtener la lista de programas de becas

    if request.method == 'POST':
        programa_id = request.POST.get('nombre')  # Obtener el ID del programa de beca seleccionado desde la solicitud(POST)

        # Obtener el programa de beca correspondiente desde la base de datos
        programa_seleccionado = get_object_or_404(ProgramaBeca, id=programa_id)

        return render(request, 'ver_programa_beca.html', {'programas': programas, 'programa_seleccionado': programa_seleccionado})
    else:
        # Si la solicitud no es POST muestra la página con la lista de programas
        return render(request, 'ver_programa_beca.html', {'programas': programas})

# Vista para seleccionar un programa de beca
def seleccionar_programa_beca(request):
    programas = ProgramaBeca.objects.all()
    
    if request.method == 'POST':
        programa_id = request.POST.get('programa_id')
        if programa_id:
            return redirect('app_login:editar_programa_beca', programa_id=programa_id)
    
    return render(request, 'seleccionar_programa_beca.html', {'programas': programas})

# Vista para editar un programa de beca
def editar_programa_beca(request, programa_id):
    programa_seleccionado = get_object_or_404(ProgramaBeca, id=programa_id)
    programas = ProgramaBeca.objects.all()
    usuarios_donantes = User.objects.filter(first_name='Donante')
    success_message = ""

    if request.method == 'POST':
        form = ProgramaBecaForm(request.POST, instance=programa_seleccionado)
        if form.is_valid():
            form.save()
            success_message = "Los cambios se han guardado exitosamente."
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = ProgramaBecaForm(instance=programa_seleccionado)

    return render(request, 'editar_programa_beca.html', {'programa_seleccionado': programa_seleccionado, 'programas': programas, 'usuarios_donantes': usuarios_donantes, 'success_message': success_message, 'form': form})
def crear_cronograma(request):
    if request.method == 'POST':
        programa_becas = request.POST['programa_becas']
        tipo_convocatoria = request.POST['tipo_convocatoria']
        fecha_inscripciones = request.POST['fecha_inscripciones']
        fecha_cierre_inscripciones = request.POST['fecha_cierre_inscripciones']
        fecha_seleccion_aspirantes = request.POST['fecha_seleccion_aspirantes']
        fecha_entrevistas = request.POST['fecha_entrevistas']
        fecha_publicacion_beneficiarios = request.POST['fecha_publicacion_beneficiarios']

        # Crea instancias de los modelos y guárdalas en la base de datos
        programa_beca_obj = ProgramaBeca.objects.create(nombre=programa_becas)
        tipo_convocatoria_obj = TipoConvocatoria.objects.create(nombre=tipo_convocatoria)
        cronograma_obj = Cronograma.objects.create(
            programa_becas=programa_beca_obj,
            tipo_convocatoria=tipo_convocatoria_obj,
            fecha_inscripciones=fecha_inscripciones,
            fecha_cierre_inscripciones=fecha_cierre_inscripciones,
            fecha_seleccion_aspirantes=fecha_seleccion_aspirantes,
            fecha_entrevistas=fecha_entrevistas,
            fecha_publicacion_beneficiarios=fecha_publicacion_beneficiarios
        )

        # Redirige a alguna página de éxito o muestra un mensaje de éxito
        return render(request, 'inicio.html')
    else:
        # Si el método de solicitud no es POST, muestra el formulario
        return render(request, 'registrar_cronograma.html')
