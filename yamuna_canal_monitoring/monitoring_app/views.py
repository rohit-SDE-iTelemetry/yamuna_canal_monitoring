from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# dashboard view
def dashboard(request):
    if request.method == 'GET':
        context = {}
        return render(request,'dashboard.html')

#########################################################################################################
# USER MODULE
#########################################################################################################
# user-list view
def user_list(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/user-list.html')

# add-user view
def add_user(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/add-user.html')

# edit-user view
def edit_user(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/edit-user.html')

#########################################################################################################
# site MODULE
#########################################################################################################
# site-list view
def site_list(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/site-list.html')

# add-site view
def add_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/add-site.html')

# edit-site view
def edit_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/edit-site.html')

#########################################################################################################
# REPORT MODULE
#########################################################################################################
def reports_dash(request):
    if request.method == 'GET':
        context = {}
        return render(request,'utils/reports.html')

#########################################################################################################
# REPORT MODULE
#########################################################################################################
def gis(request):
    if request.method == 'GET':
        context = {}
        return render(request,'gis/gis.html')
