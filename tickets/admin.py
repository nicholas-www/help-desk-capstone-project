from django.contrib import admin

from tickets.models import Ticket, TicketImage


class TicketImageInline(admin.TabularInline):
    model = TicketImage
    extra = 1  # show one empty form for uploading ticket images.


# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('sender', 'title', 'created_at', 'assigned_to', 'is_resolved')
    list_filter = ('created_at', 'assigned_to', 'is_resolved')
    ordering = ('created_at',)
    inlines = [TicketImageInline]
