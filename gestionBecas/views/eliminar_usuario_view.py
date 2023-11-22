from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class EliminarUsuarioView(View):
    def delete(self, request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return HttpResponse(status=200)
