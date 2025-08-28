import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from django.http import HttpResponse


def api_root(request):
    return HttpResponse("Welcome to the HelpDesk API. See /api/docs/ for documentation.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('tickets.urls')),
    path('api/', include('responses.urls')),

    path('api/', api_root, name='api_root'),

    # Endpoint for API Docs
    path('api/docs/', TemplateView.as_view(template_name='api_docs/markdown.html'), name='api-docs')
]

# for storing and serving media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
