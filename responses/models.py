from django.contrib.auth import get_user_model
from django.db import models

from tickets.models import Ticket

User = get_user_model()


class TicketResponse(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='ticket_response')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
