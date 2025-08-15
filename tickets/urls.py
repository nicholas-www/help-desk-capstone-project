from django.urls import path

from tickets import views

urlpatterns = [
    path('tickets/', views.TicketListAPIView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', views.TicketDetailAPIView.as_view(), name='ticket-detail')
]
