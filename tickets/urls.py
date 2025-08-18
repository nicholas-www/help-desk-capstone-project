from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from tickets import views

urlpatterns = [
    path('tickets/', views.TicketListAPIView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', views.TicketDetailAPIView.as_view(), name='ticket-detail'),
    path('tickets/create/', views.TicketCreateAPIView.as_view(), name='create-ticket')
]


# for storing and serving media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)