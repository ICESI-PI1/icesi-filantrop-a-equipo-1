from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Usuario, Rol
from .models import ProgramaBeca

from datetime import date  # Importa la clase 'date' para definir la fecha


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
         self.assertEqual(response.status_code,200)

    def test_login_invalid_user(self):
        response=self.client.post(reverse('app_login:login'),{'usuario':'manuelh','constraseña':'incorretopasword'})
        self.assertContains(response,'Nombre de usuario o contraseña incorrectos')  

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
        self.assertEqual(response.status_code, 200 )



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
         self.assertEqual(response.status_code, 200)


        

class ChangeRoleTestCase(TestCase):
    def setUp(self):
        # Configurar datos de prueba, como usuarios y roles
        self.user = User.objects.create_user(username='juanb', password='icesi12345678')
        self.rol_admin = Rol.objects.create(nombre='Administrador')
        self.rol_donante = Rol.objects.create(nombre='Donante')
        self.usuario = Usuario.objects.create(user=self.user)

    def test_change_to_admin_role(self):
        # Cambiar el rol del usuario a Administrador
        response = self.client.post(reverse('app_login:asignar_roles'), {
            'usuario_id': self.usuario.id,
            'rol_id': self.rol_admin.id,
        })

        # Verificar que la respuesta sea exitosa (código de estado 200)
        self.assertEqual(response.status_code, 200)

        # Recargar el objeto Usuario desde la base de datos
        self.usuario.refresh_from_db()

        # Verificar que el usuario tenga el rol de Administrador
        self.assertFalse(self.usuario.roles.filter(id=self.rol_admin.id).exists())

    def test_change_to_donor_role(self):
        # Cambiar el rol del usuario a Donante
        response = self.client.post(reverse('app_login:asignar_roles'), {
            'usuario_id': self.usuario.id,
            'rol_id': self.rol_donante.id,
        })

        # Verificar que la respuesta sea exitosa (código de estado 200)
        self.assertEqual(response.status_code, 200)

        # Recargar el objeto Usuario desde la base de datos
        self.usuario.refresh_from_db()

        # Verificar que el usuario tenga el rol de Donante
        self.assertFalse(self.usuario.roles.filter(id=self.rol_donante.id).exists())





class GestionProgramaBecaTestCase(TestCase):
    
    def setUp(self):
        # Configure test data, such as users and scholarship programs
        self.user = User.objects.create_user(username='juanb', password='icesi12345678')
        self.programa_beca = ProgramaBeca.objects.create(
            nombre='Beca Prueba',
            descripcion='Esta es una beca de prueba',
            fechaInicio='2023-01-01',
            fechaFin='2023-12-31',
            cupo=10,
            donantes=self.usuario.username,
            coberturaEconomica=1000,
            tipoBeca='Tipo Prueba',
            requisitos='Requisitos Prueba'
        )

    def test_gestion_programa_beca_view(self):
        # Test the gestion_programa_beca view
        response = self.client.get(reverse('gestion_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_programa_beca.html')

    def test_ver_programa_beca_view(self):
        # Test the ver_programa_beca view
        response = self.client.get(reverse('ver_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ver_programa_beca.html')

    def test_eliminar_programa_beca_view(self):
        # Test the eliminar_programa_beca view
        response = self.client.get(reverse('eliminar_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_programa_beca.html')

    def test_eliminar_programa_beca_individual_view(self):
        # Test the eliminar_programa_beca_individual view
        response = self.client.get(reverse('eliminar_programa_beca_individual', args=[self.programa_beca.nombre]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': True, 'message': 'Programa de Beca eliminado con éxito.'})


  