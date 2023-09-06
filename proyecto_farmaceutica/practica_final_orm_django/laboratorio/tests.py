from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creamos un laboratorio de ejemplo en la base de datos simulada
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')

    def test_datos_coinciden_con_setUpTestData(self):
        # Obtenemos el laboratorio creado en setUpTestData
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio 1')

        # Verificamos que los datos en la base de datos coincidan con los creados en setUpTestData
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'País 1')

    def test_respuesta_http_200_para_laboratorio(self):
        # Obtenemos la URL de detalle del laboratorio usando reverse
        url = reverse('detalle_laboratorio', args=[1])  # Suponemos que el laboratorio con ID 1 existe

        # Hacemos una petición GET a la URL y verificamos que devuelve una respuesta HTTP 200
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_respuesta_http_200_y_contenido_html_coincide(self):
        # Obtenemos la URL de detalle del laboratorio usando reverse
        url = reverse('detalle_laboratorio', args=[1])  # Suponemos que el laboratorio con ID 1 existe

        # Hacemos una petición GET a la URL
        response = self.client.get(url)
        
        # Verificamos que devuelve una respuesta HTTP 200
        self.assertEqual(response.status_code, 200)

        # Verificamos que la plantilla utilizada sea la correcta
        self.assertTemplateUsed(response, 'detalle_laboratorio.html')

        # Verificamos que el contenido HTML coincida con lo esperado
        # Puedes ajustar este contenido según el formato que hayas definido en tu plantilla
        self.assertContains(response, '<h1>Detalle de Laboratorio</h1>')
        self.assertContains(response, '<p><strong>Nombre:</strong> Laboratorio 1</p>')
        self.assertContains(response, '<p><strong>Ciudad:</strong> Ciudad 1</p>')
        self.assertContains(response, '<p><strong>País:</strong> País 1</p>')
