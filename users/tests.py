from django.contrib.auth import get_user_model
from django.test import TestCase


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
