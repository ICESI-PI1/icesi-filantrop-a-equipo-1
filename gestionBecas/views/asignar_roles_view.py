from django.views import View
from django.shortcuts import render, redirect
from gestionBecas.models import Usuario, Rol

class AsignarRolesView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        roles = Rol.objects.all()
        return render(request, 'asignar_roles.html', {'usuarios': usuarios, 'roles': roles})

    def post(self, request):
        usuario_id = request.POST.get('usuario')
        rol_id = request.POST.get('rol')
        
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            rol = Rol.objects.get(id=rol_id)
            # Asignar el rol al usuario (dependiendo de cómo esté diseñado tu modelo de datos)
            usuario.roles.add(rol)
            return redirect('asignar_roles')
        except (Usuario.DoesNotExist, Rol.DoesNotExist):
            # Manejar errores aquí si es necesario
            pass
