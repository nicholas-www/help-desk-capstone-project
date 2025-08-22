from rest_framework import serializers

from responses.models import TicketResponse


class TicketResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketResponse
        fields = '__all__'


class CreateTicketResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketResponse
        fields = ['message']
