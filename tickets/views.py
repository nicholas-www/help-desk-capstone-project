from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from tickets.models import Ticket
from tickets.permissions import IsAgent
from tickets.serializers import TicketListSerializer, CreateTicketSerializer


# Create your views here.

class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, IsAgent]
    filterset_fields = ['is_resolved', 'created_at']


class TicketDetailAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    permission_classes = [IsAuthenticated, IsAgent]


class TicketCreateAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_classes = [IsAuthenticated]
