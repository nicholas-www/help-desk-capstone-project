from django.urls import path

from responses import views

urlpatterns = [
    path('tickets/<int:ticket_id>/respond', views.CreateTicketResponseAPIView.as_view(), name='create-response')
]