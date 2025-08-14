from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Ticket(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_tickets')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.OneToOneField(User, on_delete=models.CASCADE, related_name='assigned_tickets')
    is_resolved = models.BooleanField(default=False) # To determine whether a ticket has been resolved or not

    def __str__(self):
        return f"{self.title} by {self.sender}"
