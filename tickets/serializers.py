from rest_framework import serializers

from tickets.models import Ticket


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

    def create(self, validated_data):
        return Ticket.objects.create(
            sender=self.context['request'].user,
            **validated_data
        )
