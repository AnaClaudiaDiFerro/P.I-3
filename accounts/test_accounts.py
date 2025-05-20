from django.test import TestCase
from accounts.models import CustomUser  # Seu modelo de usuário customizado

class UserRegistrationTest(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(
            email="teste@example.com",
            password="senhaSegura123",
            username="testeuser",
            nome_completo="Teste Completo"
        )
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(user.email, "teste@example.com")
