from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Usuario, Rol

class LoginTestCase(TestCase):
    def setUp(self):
        # Configura datos de prueba, como usuarios y roles
        self.user = User.objects.create_user(username='juanesb', password='icesi123456')
        self.rol = Rol.objects.create(nombre='Rol de Prueba')  # Crea un rol de prueba
        self.usuario = Usuario.objects.create(user=self.user)
        self.usuario.roles.set([self.rol])  # Establece la relación con el rol

    def test_login_valid_user(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'juanesb', 'contraseña': 'icesi123456'})
        self.assertEqual(response.status_code, 302)  # Verifica que se haya redirigido después del inicio de sesión

    def test_login_invalid_user(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'juanesb', 'contraseña': 'incorrectpassword'})
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos')  # Verifica que se muestre un mensaje de error
