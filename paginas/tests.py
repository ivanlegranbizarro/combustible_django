from django.test import SimpleTestCase
from django.urls import reverse


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse("paginas:about"))

    def test_url_about(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_about(self):
        self.assertTemplateUsed(self.response, "paginas/about.html")
        self.assertContains(self.response, "Acerca de la APP")
        self.assertNotContains(self.response, "Viva Abuja Power")
