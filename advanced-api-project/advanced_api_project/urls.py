from django.contrib import admin
from django.urls import path, include  # include needed to reference app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # routes all API endpoints
]
