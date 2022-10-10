from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from monitoring_app.utils.GLOBALS import permissionObj,exlude_permissions,get_permissions
from auth_app.models import UserProfile

# dashboard view
@login_required(login_url='/')
def dashboard(request):
    if request.method == 'GET':
        context = {}
        return render(request,'dashboard.html',context)

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
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/add-user.html',context)
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        contact = request.POST.get('contact')
        userType = request.POST.get('userType')
        demoUser = request.POST.get('demoUser')
        permissions = request.POST.get('permissions[]')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')

        print('fullname >>> ',fullname)
        print('email >>> ',email)
        print('contact >>> ',contact)
        print('contact >>> ',contact)
        print('userType >>> ',userType)
        print('demoUser >>> ',demoUser)
        print('permissions >>> ',permissions)
        print('pincode >>> ',pincode)
        print('city >>> ',city)
        print('state >>> ',state)
        print('country >>> ',country)
        print('address >>> ',address)


        exit()

# edit-user view
@login_required(login_url='/')
def edit_user(request):
    if request.method == 'GET':
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/edit-user.html',context)

# user-view view
@login_required(login_url='/')
def user_view(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/view-users.html',context)

# user-log view
@login_required(login_url='/')
def user_log(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/user-logs.html',context)

# user-profile view
@login_required(login_url='/')
def user_profile(request):
    if request.method == 'GET':
        context = {}
        return render(request,'users/user-profiles.html',context)

#########################################################################################################
# site MODULE
#########################################################################################################
# site-list view
@login_required(login_url='/')
def site_list(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/site-list.html',context)

# view-site view
@login_required(login_url='/')
def view_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/view-site.html',context)

# add-site view
@login_required(login_url='/')
def add_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/add-site.html',context)

# edit-site view
@login_required(login_url='/')
def edit_site(request):
    if request.method == 'GET':
        context = {}
        return render(request,'sites/edit-site.html',context)



#########################################################################################################
# GIS MODULE
#########################################################################################################
@login_required(login_url='/')
def gis(request):
    if request.method == 'GET':
        context = {}
        return render(request,'gis/gis.html',context)

#########################################################################################################
# GUIDELINES MODULE
#########################################################################################################
@login_required(login_url='/')
def guidelines(request):
    if request.method == 'GET':
        context = {}
        return render(request,'eyc-guidelines.html',context)

#########################################################################################################
# ALERTS MODULE
#########################################################################################################
@login_required(login_url='/')
def alerts(request):
    if request.method == 'GET':
        context = {}
        return render(request,'alerts.html',context)




