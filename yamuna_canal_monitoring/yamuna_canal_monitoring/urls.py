from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from monitoring_app.views.error_view import error404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('auth_app.urls')),
    path('',include('monitoring_app.urls')),
    path('error404',error404,name="error404"),

]

urlpatterns += staticfiles_urlpatterns()