from django.urls import path
from monitoring_app.views import *

urlpatterns = [
    path('dashboard', dashboard,name = "dashboard"),

    # reports url
    path('report', report,name = "report"),

    # user urls
    path('add-user', add_user,name = "add_user"),
    path('edit-user', edit_user,name = "edit_user"),
    path('users', user_list,name = "users"),
    path('view-user', user_view,name = "user_view"),
    path('user-log', user_log,name = "user_log"),
    path('user-profile', user_profile,name = "user_profile"),

    # site urls
    path('add-site', add_site,name = "add_site"),
    path('view-site', view_site,name = "view_site"),
    path('edit-site', edit_site,name = "edit_site"),
    path('sites', site_list,name = "sites"),

    # gis urls
    path('gis', gis,name = "gis"),

    # guidelines urls
    path('eyc-guidelines', guidelines,name = "guidelines"),

    # master urls
    path('master-pages', master,name = "master"),
    path('add-category', add_category,name = "add_category"),
    path('add-parameter', add_param,name = "add_params"),

]