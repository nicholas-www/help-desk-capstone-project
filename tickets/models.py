from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from tickets.utils import get_available_agent

# Create your models here.

User = get_user_model()


class Ticket(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_tickets')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='assigned_tickets',
        blank=True, null=True
    )

    is_resolved = models.BooleanField(default=False)  # To determine whether a ticket has been resolved or not

    def __str__(self):
        return f"{self.title}"

    def clean(self):
        if self.sender.is_agent:
            raise ValidationError("Agents are not allowed to send Tickets")

        if self.sender == self.assigned_to:
            raise ValidationError("Ticket cannot be assigned to the same sender")

    def save(self, *args, **kwargs):
        if not self.assigned_to:
            self.assigned_to = get_available_agent()
            print("assigned_to", self.assigned_to)

        self.full_clean()
        super().save(*args, **kwargs)


class TicketImage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticket_images')
    image = models.ImageField(upload_to='ticket_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Ticket({self.ticket.id})"
