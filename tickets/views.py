from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.permissions import IsAgent
from tickets.serializers import TicketListSerializer, CreateTicketSerializer, UserTicketListSerializer


# Create your views here.

class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, IsAgent]
    filterset_fields = ['is_resolved', 'created_at']


class UserTicketListAPIView(generics.ListAPIView):
    serializer_class = UserTicketListSerializer
    filterset_fields = ['is_resolved', 'created_at']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(sender=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')

        if user_id != request.user.id:
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

        if request.user.is_agent:
            return Response({'error': 'Agents do not send tickets'}, status=status.HTTP_403_FORBIDDEN)

        return super().list(request, *args, **kwargs)


class TicketDetailAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    permission_classes = [IsAuthenticated, IsAgent]


class TicketCreateAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_classes = [IsAuthenticated]
