from django.urls import path
from monitoring_app.views import *

urlpatterns = [
    path('dashboard', dashboard,name = "dashboard"),
    path('reports_dash', reports_dash,name = "reports_dash"),

    # user urls
    path('add-user', add_user,name = "add_user"),
    path('edit-user', edit_user,name = "edit_user"),
    path('users', user_list,name = "users"),

    # site urls
    path('add-site', add_site,name = "add_site"),
    path('edit-site', edit_site,name = "edit_site"),
    path('sites', site_list,name = "sites"),

    # gis urls
    path('gis', gis,name = "gis"),

]