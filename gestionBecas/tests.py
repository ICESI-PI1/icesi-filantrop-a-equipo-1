from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Usuario, Rol


class LoginTestCase(TestCase):
    def setUp(self):
        # Configura datos de prueba, como usuarios y roles
        self.user = User.objects.create_user(username='juanesb', password='icesi123456')
        self.user=User.objects.create_user(username='manuelh',password='icesi12345678')
        self.rol = Rol.objects.create(nombre='Rol de Prueba')  # Crea un rol de prueba
        self.usuario = Usuario.objects.create(user=self.user)
        self.usuario.roles.set([self.rol])  # Establece la relación con el rol

    def test_login_valid_user(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'juanesb', 'contraseña': 'icesi123456'})
        self.assertEqual(response.status_code, 302)  # Verifica que se haya redirigido después del inicio de sesión

    def test_login_invalid_user(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'juanesb', 'contraseña': 'incorrectpassword'})
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos')  # Verifica que se muestre un mensaje de error

    def test_login_valid_user2(self):
         response=self.client.post(reverse('app_login:login'),{'usuario':'manuelh','contrseña':'icesi12345678'})
         self.assertEqual(response.status_code,302)

    def test_login_invalid_user(self):
        response=self.client.post(reverse('app_login:login'),{'usuario':'manuelh','constraseña':'incorretopasword'})) 
        self.assertContains(response,'nombre de usuario o contraseña incorrectos')  

    def test_login_nonexistent_user(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'noexiste', 'contraseña': 'icesi123456'})
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos')  # Verifica que se muestre un mensaje de error

    def test_login_empty_username(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': '', 'contraseña': 'icesi123456'})
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos')  # Verifica que se muestre un mensaje de error

    def test_login_empty_password(self):
        response = self.client.post(reverse('app_login:login'), {'usuario': 'juanesb', 'contraseña': ''})
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos')  # Verifica que se muestre un mensaje de error


        



class RegistrationTestCase(TestCase):
    def test_register_valid_user(self):
        # Datos de usuario de prueba
        username = 'nuevo_usuario'
        password = 'nueva_contraseña'
        email = 'juan@example.com'

        # Realizar una solicitud POST a la vista de registro
        response = self.client.post(reverse('app_login:signup'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
        })

        # Verificar que se haya redirigido después del registro (éxito)
        self.assertEqual(response.status_code, 302)

        # Verificar que el usuario se haya creado en la base de datos
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_register_invalid_user(self):
        # Datos de usuario de prueba con contraseña incorrecta
        username = 'nuevo_usuario'
        password = 'contraseña_invalida'
        email = 'juan@example.com'

        # Realizar una solicitud POST a la vista de registro con contraseña incorrecta
        response = self.client.post(reverse('app_login:signup'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
        })

        # Verificar que se haya redirigido nuevamente a la página de registro debido a una contraseña incorrecta
        self.assertEqual(response.status_code, 302)

    def test_register_short_username(self):
        # Datos de usuario con nombre de usuario demasiado corto
        username = 'nu'
        password = 'nueva_contraseña'
        email = 'juan@example.com'

        # Intentar registrar un nuevo usuario con nombre de usuario demasiado corto
        response = self.client.post(reverse('app_login:signup'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
        })

        # Verificar que se haya redirigido nuevamente a la página de registro debido a un nombre de usuario demasiado corto
        self.assertEqual(response.status_code, 302)

    def test_register_short_password(self):
        # Datos de usuario con contraseña demasiado corta
        username = 'nuevo_usuario'
        password = '123'
        email = 'juan@example.com'

        # Intentar registrar un nuevo usuario con contraseña demasiado corta
        response = self.client.post(reverse('app_login:signup'), {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
        })

        # Verificar que se haya redirigido nuevamente a la página de registro debido a una contraseña demasiado corta
        self.assertEqual(response.status_code, 302)



    def test_register_without_username(self):
         # Datos de usuario sin proporcionar un nombre de usuario
         username = ''
         password = 'nueva_contraseña'
         email = 'juan@example.com'

         # Intentar registrar un nuevo usuario sin proporcionar un nombre de usuario
         response = self.client.post(reverse('app_login:signup'), {
             'username': username,
             'password1': password,
             'password2': password,
             'email': email,
         })

         # Verificar que se haya redirigido nuevamente a la página de registro debido a no proporcionar un nombre de usuario
         self.assertEqual(response.status_code, 302)
  
        

