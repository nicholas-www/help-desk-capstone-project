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
        return Ticket(
            sender=self.context['request'].user,
            title=validated_data['title'],
            description=validated_data['description']
        )
