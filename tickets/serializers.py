from rest_framework import serializers

from tickets.models import Ticket, TicketImage


class TicketImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketImage
        fields = ['image']

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'



class CreateTicketSerializer(serializers.ModelSerializer):
    ticket_images = TicketImageSerializer(many=True, required=False)
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'ticket_images']

    def create(self, validated_data):
        return Ticket.objects.create(
            sender=self.context['request'].user,
            **validated_data
        )
