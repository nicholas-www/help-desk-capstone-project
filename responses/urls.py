from django.urls import path

from responses import views

urlpatterns = [
    path('tickets/<int:ticket_id>', views.CreateTicketResponseAPIView.as_view(), name='create-response')
]