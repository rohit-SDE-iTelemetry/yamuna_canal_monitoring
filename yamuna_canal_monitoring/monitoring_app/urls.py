from django.urls import path
from monitoring_app.views import dashboard,reports_dash

urlpatterns = [
    path('dashboard', dashboard,name = "dashboard"),
    path('reports_dash', reports_dash,name = "reports_dash"),

]