from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from monitoring_app.utils.GLOBALS import permissionObj,exlude_permissions,get_permissions
from auth_app.models import UserProfile


#########################################################################################################
# 404 Error page
#########################################################################################################
def error404(request):
    if request.method == 'GET':
        context = {}
        return render(request,'errorPages/404error.html',context)

#########################################################################################################
# DSS MODULE
#########################################################################################################
@login_required(login_url='/')
def decision_support_system(request):
    if request.method == 'GET':
        context = {}
        return render(request,'dss/dss-dashboard.html',context)