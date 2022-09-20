from django.urls import path
from auth_app.views.views import login

urlpatterns = [
    path('', login),
]