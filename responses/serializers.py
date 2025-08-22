from rest_framework import serializers

from responses.models import TicketResponse


class CreateTicketResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketResponse
        fields = ['message']

