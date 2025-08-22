from django.contrib import admin

from responses.models import TicketResponse


# Register your models here.

@admin.register(TicketResponse)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'sender')

