from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Usuario, Rol
from .models import ProgramaBeca
from django.utils import timezone
from . import views
from datetime import date  # Importa la clase 'date' para definir la fecha
from gestionBecas.models import Cronograma

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
        response = self.client.post(reverse('app_login:asignar_roles_view'), {
            'usuario_id': self.usuario.id,
            'rol_id': self.rol_admin.id,
        })

        # Verificar que la respuesta sea exitosa (código de estado 200)
        self.assertEqual(response.status_code, 200)

        # Recargar el objeto Usuario desde la base de datos
        self.usuario.refresh_from_db()

        # Verificar que el usuario tenga el rol de Administrador
        self.assertFalse(self.usuario.roles.filter(id=self.rol_admin.id).exists())

    





class GestionProgramaBecaTestCase(TestCase):
    
    def setUp(self):
        # Configura datos de prueba, como usuarios y programas de becas
        self.user = User.objects.create_user(username='juanb', password='icesi12345678')
        self.programa_beca = ProgramaBeca.objects.create(
            nombre='Beca Prueba',
            descripcion='Esta es una beca de prueba',
            fechaInicio='2023-01-01',
            fechaFin='2023-12-31',
            cupo=10,
            donantes=self.user.username,
            coberturaEconomica=1000,
            tipoBeca='Tipo Prueba',
            requisitos='Requisitos Prueba'
        )

    def test_gestion_programa_beca_view(self):
        # Prueba la vista gestion_programa_beca
        response = self.client.get(reverse('app_login:gestion_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gestion_programa_beca.html')

    def test_ver_programa_beca_view(self):
        # Prueba la vista ver_programa_beca
        response = self.client.get(reverse('app_login:ver_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ver_programa_beca.html')

    def test_eliminar_programa_beca_view(self):
        # Prueba la vista eliminar_programa_beca
        response = self.client.get(reverse('app_login:eliminar_programa_beca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_programa_beca.html')

    def test_eliminar_programa_beca_individual_view(self):
    # Test the eliminar_programa_beca_individual view
        response = self.client.get(reverse('app_login:eliminar_programa_beca_individual', args=[self.programa_beca.id]))
        self.assertEqual(response.status_code, 405)
        expected_data = {'success': True, 'message': 'Programa de Beca eliminado con éxito.'}
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_data)

    def test_ver_programa_beca(self):
        response = self.client.get(reverse('app_login:ver_programa_beca'))
        self.assertEqual(response.status_code, 200)
       
class EditarProgramaBecaViewTest(TestCase):
    
    def setUp(self):
        fecha_inicio = timezone.now()  # Usa la fecha y hora actual
        fecha_fin = fecha_inicio + timezone.timedelta(days=30)  # Añade 30 días a la fecha de inicio
        cupo=10
        coberturaEconomica=1000
        tipoBeca='Tipo Prueba'
        requisitos='Requisitos Prueba'
        self.programa_beca = ProgramaBeca.objects.create(nombre='Programa de prueba', fechaInicio=fecha_inicio, fechaFin=fecha_fin,cupo=cupo,coberturaEconomica=coberturaEconomica,tipoBeca=tipoBeca,requisitos=requisitos)
        self.donante = User.objects.create_user(username='donante', password='donante123', first_name='Donante')

    def test_get_editar_programa_beca_view_with_valid_id(self):
        response = self.client.get(reverse('app_login:editar_programa_beca', args=[self.programa_beca.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_programa_beca.html')

    def test_get_editar_programa_beca_view_with_invalid_id(self):
        response = self.client.get(reverse('app_login:editar_programa_beca', args=[999]))
        self.assertEqual(response.status_code, 404)


    def test_post_editar_programa_beca_view_with_invalid_form_data(self):
        form_data = {'nombre': '', 'fechaInicio': '', 'fechaFin': '', 'cupo': '', 'coberturaEconomica': '', 'tipoBeca': '', 'requisitos': ''}
        response = self.client.post(reverse('app_login:editar_programa_beca', args=[self.programa_beca.id]), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_programa_beca.html')

    def test_get_editar_programa_beca_view_with_donante_user(self):
        self.client.login(username='donante', password='donante123')
        response = self.client.get(reverse('app_login:editar_programa_beca', args=[self.programa_beca.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_programa_beca.html')



class CrearCronogramaViewTest(TestCase):
    
    def setUp(self):
        fecha_inicio = timezone.now()  # Usa la fecha y hora actual
        fecha_fin = fecha_inicio + timezone.timedelta(days=30)  # Añade 30 días a la fecha de inicio
        cupo=10
        coberturaEconomica=1000
        tipoBeca='Tipo Prueba',
        requisitos='Requisitos Prueba'
        self.programa_beca = ProgramaBeca.objects.create(nombre='Programa de prueba', fechaInicio=fecha_inicio, fechaFin=fecha_fin,cupo=cupo,coberturaEconomica=coberturaEconomica,tipoBeca=tipoBeca,requisitos=requisitos)
        
   
    def test_get_crear_cronograma_view(self):
        response = self.client.get(reverse('app_login:registrar_cronograma', args=[self.programa_beca.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_cronograma.html')


    def test_post_invalid_form_crear_cronograma_view(self):
        form_data = {'nombre': ''}
        response = self.client.post(reverse('app_login:registrar_cronograma', args=[self.programa_beca.id]), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_cronograma.html')

    def test_post_nonexistent_programa_beca_crear_cronograma_view(self):
        form_data = {'nombre': 'Cronograma de prueba', 'programa_becas': 999}
        response = self.client.post(reverse('app_login:registrar_cronograma', args=[999]), form_data)
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_programa_beca_crear_cronograma_view(self):
        response = self.client.get(reverse('app_login:registrar_cronograma', args=[999]))
        self.assertEqual(response.status_code, 404)



class CronogramaViewTest(TestCase):
    
    def setUp(self):
        fecha_inicio = timezone.now()  # Usa la fecha y hora actual
        fecha_fin = fecha_inicio + timezone.timedelta(days=30)  # Añade 30 días a la fecha de inicio
        cupo=10
        coberturaEconomica=1000
        tipoBeca='Tipo Prueba'
        requisitos='Requisitos Prueba'
        self.programa_beca1 = ProgramaBeca.objects.create(nombre='Programa de prueba', fechaInicio=fecha_inicio, fechaFin=fecha_fin,cupo=cupo,coberturaEconomica=coberturaEconomica,tipoBeca=tipoBeca,requisitos=requisitos)
        self.programa_beca2 = ProgramaBeca.objects.create(nombre='Programa de prueba 2', fechaInicio=fecha_inicio, fechaFin=fecha_fin,cupo=cupo,coberturaEconomica=coberturaEconomica,tipoBeca=tipoBeca,requisitos=requisitos)
        self.cronograma1 = Cronograma.objects.create(programa_becas=self.programa_beca1, tipo_convocatoria='Abierta', fecha_inscripciones=fecha_inicio, fecha_cierre_inscripciones=fecha_fin, fecha_seleccion_aspirantes=fecha_fin, fecha_entrevistas=fecha_fin, fecha_publicacion_beneficiarios=fecha_fin)
        self.cronograma2 = Cronograma.objects.create(programa_becas=self.programa_beca2, tipo_convocatoria='Mixta', fecha_inscripciones=fecha_inicio, fecha_cierre_inscripciones=fecha_fin, fecha_seleccion_aspirantes=fecha_fin, fecha_entrevistas=fecha_fin, fecha_publicacion_beneficiarios=fecha_fin)

    def test_get_eliminar_cronograma_view(self):
        response = self.client.get(reverse('app_login:eliminar_cronograma'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_cronograma.html')
        self.assertEqual(len(response.context['cronogramas']), 2)

    def test_delete_request_with_valid_cronograma_id(self):
        response = self.client.delete(reverse('app_login:eliminar_cronograma_individual', args=[self.cronograma1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True, 'message': 'Cronograma eliminado con éxito.'})
        with self.assertRaises(Cronograma.DoesNotExist):
            Cronograma.objects.get(id=self.cronograma1.id)

    def test_delete_request_with_invalid_cronograma_id(self):
        response = self.client.delete(reverse('app_login:eliminar_cronograma_individual', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': False, 'message': 'El cronograma no existe.'})

    def test_delete_request_with_second_valid_cronograma_id(self):
        response = self.client.delete(reverse('app_login:eliminar_cronograma_individual', args=[self.cronograma2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True, 'message': 'Cronograma eliminado con éxito.'})
        with self.assertRaises(Cronograma.DoesNotExist):
            Cronograma.objects.get(id=self.cronograma2.id)

    def test_get_eliminar_cronograma_view_after_deletion(self):
        self.client.delete(reverse('app_login:eliminar_cronograma_individual', args=[self.cronograma1.id]))
        self.client.delete(reverse('app_login:eliminar_cronograma_individual', args=[self.cronograma2.id]))
        response = self.client.get(reverse('app_login:eliminar_cronograma'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_cronograma.html')
        self.assertEqual(len(response.context['cronogramas']), 0)



class EditarCronogramaViewTest(TestCase):
    
    def setUp(self):
        fecha_inicio = timezone.now()  # Usa la fecha y hora actual
        fecha_fin = fecha_inicio + timezone.timedelta(days=30)  # Añade 30 días a la fecha de inicio
        cupo=10
        coberturaEconomica=1000
        tipoBeca='Tipo Prueba'
        requisitos='Requisitos Prueba'
        self.programa_beca = ProgramaBeca.objects.create(nombre='Programa de prueba', fechaInicio=fecha_inicio, fechaFin=fecha_fin,cupo=cupo,coberturaEconomica=coberturaEconomica,tipoBeca=tipoBeca,requisitos=requisitos)
        self.cronograma = Cronograma.objects.create(programa_becas=self.programa_beca, tipo_convocatoria='Abierta', fecha_inscripciones=fecha_inicio, fecha_cierre_inscripciones=fecha_fin, fecha_seleccion_aspirantes=fecha_fin, fecha_entrevistas=fecha_fin, fecha_publicacion_beneficiarios=fecha_fin)

    def test_get_editar_cronograma_view_with_valid_id(self):
        response = self.client.get(reverse('app_login:editar_cronograma', args=[self.cronograma.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_cronograma.html')

    def test_get_editar_cronograma_view_with_invalid_id(self):
        response = self.client.get(reverse('app_login:editar_cronograma', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_editar_cronograma_view_with_valid_form_data(self):
        form_data = {'programa_becas': self.programa_beca.id, 'tipo_convocatoria': 'Mixta'}
        response = self.client.post(reverse('app_login:editar_cronograma', args=[self.cronograma.id]), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_cronograma.html')
        self.cronograma.refresh_from_db()
        self.assertEqual(self.cronograma.tipo_convocatoria, 'Abierta')

    def test_post_editar_cronograma_view_with_invalid_form_data(self):
        form_data = {'programa_becas': '', 'tipo_convocatoria': ''}
        response = self.client.post(reverse('app_login:editar_cronograma', args=[self.cronograma.id]), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_cronograma.html')






