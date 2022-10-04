from django.urls import path
from auth_app.views.views import signin, logout_view

urlpatterns = [
    path('', signin),
    path('logout', logout_view,name='logout_view'),
]