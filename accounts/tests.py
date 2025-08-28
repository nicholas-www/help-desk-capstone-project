from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin = User.objects.create_superuser(
            email='admin@gmail.com',
            first_name='Admin',
            last_name='User',
            date_of_birth='1990-01-01',
            password='pass123'
        )
        self.admin_token = Token.objects.create(user=self.admin)

    def test_customer_creation(self):
        """ To test the registration of normal users """

        url = reverse('register-customer')

        data = {
            'email': 'user@gmail.com',
            'first_name': 'Test',
            'last_name': 'User',
            'date_of_birth': '1990-01-01',
            'password': 'pass@123',
            'password2': 'pass@123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_agent_registration(self):
        """ To test the registration agents """

        url = reverse('register-agent')
        # Set Authorization token since only admins can create agents
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token}')

        data = {
            'email': 'agent@gmail.com',
            'first_name': 'Test',
            'last_name': 'Agent',
            'date_of_birth': '1990-01-01',
            'password': 'pass@123',
            'password2': 'pass@123',
            'is_active': True
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
