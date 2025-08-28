from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth import get_user_model
from tickets.models import Ticket

User = get_user_model()

class TicketResponseTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin = User.objects.create_superuser(
            email="admin@example.com",
            first_name="Test",
            last_name="Admin",
            date_of_birth="1990-01-01",
            password="pass@123",
        )
        self.admin_token = Token.objects.create(user=self.admin)

        self.user = User.objects.create_user(
            email="user@example.com",
            first_name="Test",
            last_name="User",
            date_of_birth="1990-01-01",
            password="pass@123",
        )
        self.user_token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_token}")

        self.ticket = Ticket.objects.create(
            sender=self.user,
            title="Login Issue",
            description="Can't login"
        )

    def test_ticket_response_creation(self):
        """Agent can respond to a ticket and resolve it"""
        url = reverse("create-response", kwargs={"ticket_id": self.ticket.id})
        data = {"message": "We have reset your password, try again."}

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token}")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Ticket resolved successfully")

        # Mark ticket is resolved
        self.ticket.refresh_from_db()
        self.assertTrue(self.ticket.is_resolved)

    def test_ticket_response_already_resolved(self):
        """Cannot respond twice to the same ticket"""
        # First response
        url = reverse("create-response", kwargs={"ticket_id": self.ticket.id})
        data = {"message": "First response"}
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token}")
        self.client.post(url, data, format="json")

        # 2nd
        response = self.client.post(url, {"message": "Second response"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This Ticket has already been resolved", str(response.data))

    def test_ticket_response_unauthorized(self):
        """Unauthorized users cannot respond"""
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_token}")
        url = reverse("create-response", kwargs={"ticket_id": self.ticket.id})
        response = self.client.post(url, {"message": "Unauthorized attempt"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
