from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

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
        # Prevent the creating of multiple responses for the same ticket
        if ticket.is_resolved:
            return Response(
                {'error': 'This Ticket has already been resolved'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Set the title of the response to the title of the ticket
        title = f"RES: {ticket.title.upper()}"

        serializer.save(
            ticket=ticket,
            sender=self.request.user,
            title=title
        )

        # Update the is_resolved status of the ticket
        ticket.is_resolved = True
        ticket.save()
