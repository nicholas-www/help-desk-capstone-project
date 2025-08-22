from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from responses.models import TicketResponse
from responses.serializers import CreateTicketResponseSerializer
from tickets.models import Ticket
from tickets.permissions import IsAgent


class CreateTicketResponseAPIView(generics.CreateAPIView):
    serializer_class = CreateTicketResponseSerializer
    permission_classes = [IsAgent]  # Only Agents are allowed to respond to tickets

    def perform_create(self, serializer):
        # Get ticket id from the url i.e api/tickets/<int:id>/respond
        ticket_id = self.kwargs.get('ticket_id')

        ticket = get_object_or_404(Ticket, id=ticket_id)

        # Set the title of the response to the title of the ticket
        title = f"RES: {ticket.title.upper()}"

        TicketResponse.objects.create(
            ticket=ticket,
            sender=self.request.user,
            title=title
        )

        # Update the is_resolved status
        ticket.is_resolved = True
