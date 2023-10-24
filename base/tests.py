from django.test import SimpleTestCase
from django.urls import reverse


class SimpleTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse("base:home"))

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template_home(self):
        self.assertTemplateUsed(self.response, "base/home.html")

    def test_home_page_contains_inicio(self):
        self.assertContains(self.response, "Inicio")
