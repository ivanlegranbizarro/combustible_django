from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import UserCreationForm
from .views import SignUp


class CustomUserTests(TestCase):
    def test_create_user(self):
        UserModel = get_user_model()
        new_user = UserModel.objects.create_user(
            username="testinguser", email="testing@testing.com", password="123456"
        )
        self.assertEqual(new_user.username, "testinguser")
        self.assertEqual(new_user.email, "testing@testing.com")
        self.assertTrue(new_user.check_password("123456"))
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)

    def test_create_super_user(self):
        UserModel = get_user_model()
        new_user = UserModel.objects.create_superuser(
            username="superuser", email="super@super.com", password="123456"
        )
        self.assertEqual(new_user.username, "superuser")
        self.assertEqual(new_user.email, "super@super.com")
        self.assertTrue(new_user.check_password("123456"))
        self.assertTrue(new_user.is_active)
        self.assertTrue(new_user.is_staff)
        self.assertTrue(new_user.is_superuser)


class RegistroUsuarioTest(TestCase):
    def setUp(self):
        url = reverse("users:signup")
        self.response = self.client.get(url)

    def test_plantilla_registro(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Regístrate")

    def test_formulario(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, UserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_registro_vista(self):
        view = resolve("/users/signup/")
        self.assertEqual(view.func.__name__, SignUp.as_view().__name__)
