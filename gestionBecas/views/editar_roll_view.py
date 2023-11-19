from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User

class EditarRollNameView(View):
    
    def post(self, request, username):
        usuario = get_object_or_404(User, username=username)
        nuevo_first_name = request.POST.get('first_name')
        if nuevo_first_name:
            usuario.first_name = nuevo_first_name
            usuario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'El campo first_name no puede estar vacío.'})
        
