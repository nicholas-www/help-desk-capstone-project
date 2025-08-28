from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model
from tickets.models import Ticket

User = get_user_model()


class TicketTest(TestCase):
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

        self.user = User.objects.create_user(
            email='user@gmail.com',
            first_name='Test',
            last_name='User',
            date_of_birth='2006-01-01',
            password='pass123'
        )
        self.user_token = Token.objects.create(user=self.user)

    def test_admin_cannot_create_ticket(self):
        """ No admin or agent can create a ticket """
        url = reverse('create-ticket')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token}')

        data = {
            'title': 'Test Ticket Creation',
            'description': 'Test Description'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_customer_ticket_creation(self):
        """ Test customer ticket creation """

        url = reverse('create-ticket')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token}')

        data = {
            'title': 'Test Ticket Creation',
            'description': 'Test Description'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
