from django.urls import path
from monitoring_app.views.views import *
from monitoring_app.views.report_view import *
from monitoring_app.views.master_view import *
from monitoring_app.views.dss_ws_view import *

urlpatterns = [
    path('dashboard', dashboard,name = "dashboard"),
    path('site-info/<uuid:uuid>', siteinfo_data,name = "siteinfo_data"),
    path('site-check/<uuid:uuid>', site_check, name="site_check"),

    # reports url
    path('report', report, name = "report"),
    path('report-filter', report_filter, name="report_filter"),

    # user urls
    path('user-management/add-user', add_user,name = "add_user"),
    path('user-management/edit-user', edit_user,name = "edit_user"),
    path('user-management/users', user_list,name = "users"),
    path('user-management/view-user/<str:uuid>', user_view,name = "user_view"),
    path('user-management/user-log', user_log,name = "user_log"),
    path('user-management/user-profile', user_profile,name = "user_profile"),

    # site urls
    path('add-site', add_site,name = "add_site"),
    path('view-site/<uuid:uuid>', view_site,name = "view_site"),
    path('edit-site', edit_site,name = "edit_site"),
    path('sites', site_list,name = "sites"),

    # gis urls
    path('gis', gis,name = "gis"),

    # guidelines urls
    path('eyc-guidelines', guidelines,name = "guidelines"),

    # alerts urls
    path('alerts', alerts,name = "alerts"),

    # master urls
    path('master-pages', master,name = "master"),
    path('add-category', add_category,name = "add_category"),
    path('add-parameter', add_param,name = "add_params"),

    # water scheduling urls
    path('water-scheduling', water_scheduling,name = "water_scheduling"),

    # dss urls
    path('decision-support-system', decision_support_system,name = "decision_support_system"),

]