from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from monitoring_app.utils.GLOBALS import exlude_permissions


# dashboard view
@login_required(login_url='/')
def dashboard(request):
    if request.method == 'GET':
        context = {}
        return render(request,'dashboard.html')

#########################################################################################################
# USER MODULE
#########################################################################################################
# user-list view
@login_required(login_url='/')
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {'users':users}
        return render(request,'users/user-list.html',context)

# add-user view
@login_required(login_url='/')
def add_user(request):
    if request.method == 'GET':
        permissionObj = Permission.objects.all()
        
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/add-user.html',context)

# edit-user view
@login_required(login_url='/')
def edit_user(request):
    if request.method == 'GET':
        permissionObj = Permission.objects.all()
        
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/edit-user.html',context)

# user-view view
@login_required(login_url='/')
def user_view(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/view-users.html')

# user-log view
@login_required(login_url='/')
def user_log(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/user-logs.html')

# user-profile view
@login_required(login_url='/')
def user_profile(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/user-profiles.html')

#########################################################################################################
# site MODULE
#########################################################################################################
# site-list view
@login_required(login_url='/')
def site_list(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/site-list.html')

# view-site view
@login_required(login_url='/')
def view_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/view-site.html')

# add-site view
@login_required(login_url='/')
def add_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/add-site.html')

# edit-site view
@login_required(login_url='/')
def edit_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/edit-site.html')

#########################################################################################################
# REPORT MODULE
#########################################################################################################
@login_required(login_url='/')
def report(request):
    if request.method == 'GET':
        context = {}
        return render(request,'reports/report.html')

#########################################################################################################
# GIS MODULE
#########################################################################################################
@login_required(login_url='/')
def gis(request):
    if request.method == 'GET':
        context = {}
        return render(request,'gis/gis.html')

#########################################################################################################
# GUIDELINES MODULE
#########################################################################################################
@login_required(login_url='/')
def guidelines(request):
    if request.method == 'GET':
        context = {}
        return render(request,'eyc-guidelines.html')

#########################################################################################################
# MASTER MODULE
#########################################################################################################
# add station category view
@login_required(login_url='/')
def master(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/master-view.html')

# add station category view
@login_required(login_url='/')
def add_category(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/add-category.html')

# add params view
@login_required(login_url='/')
def add_param(request):
    if request.method == 'GET':
        context = {}
        return render(request,'master/add-params.html')
