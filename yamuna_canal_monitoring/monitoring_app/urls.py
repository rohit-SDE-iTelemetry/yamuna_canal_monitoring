from django.urls import path
from monitoring_app.views import dashboard

urlpatterns = [
    path('dashboard', dashboard),
]