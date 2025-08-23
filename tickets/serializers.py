from rest_framework import serializers

from responses.serializers import TicketResponseSerializer
from tickets.models import Ticket, TicketImage


class TicketImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketImage
        fields = ['image']


class TicketListSerializer(serializers.ModelSerializer):
    ticket_images = TicketImageSerializer(read_only=True, many=True)
    ticket_responses = TicketResponseSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class UserTicketListSerializer(serializers.ModelSerializer):
    ticket_images = TicketImageSerializer(read_only=True, many=True)
    ticket_responses = TicketResponseSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):
    ticket_images = TicketImageSerializer(many=True, required=False)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'ticket_images']

    def create(self, validated_data):
        images = validated_data.pop('ticket_images', [])  # fetch uploaded images or assign an empty list

        ticket = Ticket.objects.create(
            sender=self.context['request'].user,
            **validated_data
        )

        for image in images:
            TicketImage.objects.create(ticket=ticket, image=image)

        return ticket
