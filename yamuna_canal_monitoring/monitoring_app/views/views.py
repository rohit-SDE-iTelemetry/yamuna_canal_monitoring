from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from monitoring_app.utils.GLOBALS import permissionObj,exlude_permissions,get_permissions
from auth_app.models import UserProfile
from monitoring_app.models import *
from monitoring_app.utils import utils
# dashboard view
@login_required(login_url='/')
def dashboard(request):
    if request.method == 'GET':
        context = {}
        if request.user.is_superuser:
            for i in SiteInfo.objects.all():
                status = utils.check_site_status(i)
                i.site_status = status
                i.save()
            context['sites'] = SiteInfo.objects.all()
            context['live_sites'] = Site.objects.filter(site_status='Live').count()
            context['delay_sites'] = Site.objects.filter(site_status='Delay').count()
            context['offline_sites'] = Site.objects.filter(site_status='Offline').count()
            context['disabled_sites'] = Site.objects.filter(site_status='Disabled').count()
            context['nat_sites'] = Site.objects.filter(site_status='No Record Availabe').count()
            context['last_reading'] = Reading2022.objects.latest('timestamp')

        return render(request,'dashboard.html',context)


@login_required(login_url='/')
def siteinfo_data(request,uuid):
    if request.method == 'GET':
        context = {}
        if request.user.is_superuser:
            SiteInfo_list = serializers.serialize('json', SiteInfo.objects.filter(uuid=uuid))
            return JsonResponse({"response" : json.loads(SiteInfo_list)})


#########################################################################################################
# USER MODULE
#########################################################################################################
# user-list view
@login_required(login_url='/')
def user_list(request):
    if request.method == 'GET':
        # users = User.objects.all()
        users = UserProfile.objects.all()
        context = {'users':users}
        return render(request,'users/user-list.html',context)

# add-user view
@login_required(login_url='/')
def add_user(request):
    if request.method == 'GET':
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/add-user.html',context)
    
    if request.method == 'POST':
        user_fullname = request.POST.get('fullname')
        user_email = request.POST.get('email')
        user_contact = request.POST.get('contact')
        user_userType = request.POST.get('userType')
        user_demoUser = request.POST.get('demoUser')
        user_permissions = request.POST.get('permissions[]')
        user_pincode = request.POST.get('pincode')
        user_city = request.POST.get('city')
        user_state = request.POST.get('state')
        user_country = request.POST.get('country')
        user_address = request.POST.get('address')

        user_permissions = user_permissions.split(',')

        print('fullname >>> ',user_fullname)
        print('email >>> ',user_email)
        print('contact >>> ',user_contact)
        print('contact >>> ',user_contact)
        print('userType >>> ',user_userType)
        print('demoUser >>> ',user_demoUser)
        print('permissions >>> ',user_permissions)
        print('pincode >>> ',user_pincode)
        print('city >>> ',user_city)
        print('state >>> ',user_state)
        print('country >>> ',user_country)
        print('address >>> ',user_address)
        message = 'success'

        # try:

        if(user_userType == '2'):
            demoUser = True
            userObj = User.objects.create(first_name = user_fullname,username = user_email,email = user_email,password = 'Eyc@12345',is_staff = True,is_active = True)
            userObj.save()

            new_user = UserProfile.objects.create(user=userObj,
                                                name=user_fullname,
                                                phone=user_contact,
                                                user_type=user_userType,
                                                demo_user=demoUser,
                                                address=user_address,
                                                zipcode=user_pincode,
                                                state=user_state,
                                                city=user_city,
                                                country=user_country
                                                )
        elif(user_userType == '1'):
            demoUser = False
            userObj = User.objects.create(first_name = user_fullname,username = user_email,email = user_email,password = 'Eyc@12345',is_staff = False,is_active = True)
            userObj.save()

            new_user = UserProfile.objects.create(user=userObj,
                                                name=user_fullname,
                                                phone=user_contact,
                                                user_type=user_userType,
                                                demo_user=demoUser,
                                                address=user_address,
                                                zipcode=user_pincode,
                                                state=user_state,
                                                city=user_city,
                                                country=user_country
                                                )

        print('message >>>> ',message)
        return JsonResponse({'message':message})




# edit-user view
@login_required(login_url='/')
def edit_user(request):
    if request.method == 'GET':
        context = {'permissionObj':permissionObj,'exlude_permissions':exlude_permissions}
        return render(request,'users/edit-user.html',context)

# user-view view
@login_required(login_url='/')
def user_view(request,uuid):
    if request.method == 'GET':
        print('uuid >>>> ',uuid)
        userinfo = get_object_or_404(UserProfile, uuid=uuid)
        context = {'userinfo':userinfo}
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
        context['sites'] = Site.objects.all()
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
        context['site_category'] = Category.objects.all()
        return render(request,'sites/add-site.html',context)
    
    if request.method == 'POST':
        station_name = request.POST.get('station_name')
        email = request.POST.get('email')
        site_id = request.POST.get('site_id')
        version = request.POST.get('version')
        contact = request.POST.get('contact')
        prefix = request.POST.get('prefix')
        sec_email = request.POST.get('sec_email')
        sec_contact = request.POST.get('sec_contact')
        siteType = request.POST.get('siteType')
        demosite = request.POST.get('demosite')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        lattitude = request.POST.get('lattitude')
        longitude = request.POST.get('longitude')
        data2nic = request.POST.get('data2nic')
        nic_alert_email = request.POST.get('nic_alert_email')
        data2sdc = request.POST.get('data2sdc')
        sdc_alert_email = request.POST.get('sdc_alert_email')
        data2ce = request.POST.get('data2ce')
        ce_alert_email = request.POST.get('ce_alert_email')
        data2wims = request.POST.get('data2wims')
        enc_key = request.POST.get('enc_key')
        prv_key = request.POST.get('prv_key')
        pub_key = request.POST.get('pub_key')
        sinage = request.POST.get('sinage')
        sms_alert = request.POST.get('sms_alert')
        email_alert = request.POST.get('email_alert')
        watsapp_alert = request.POST.get('watsapp_alert')
        delay_hr = request.POST.get('delay_hr')
        offline_hr = request.POST.get('offline_hr')

        print("station_name", station_name)
        print("email", email)
        print("site_id", site_id)
        print("version", version)
        print("contact", contact)
        print("prefix", prefix)
        print("sec_email", sec_email)
        print("sec_contact", sec_contact)
        print("siteType", siteType)
        print("demosite", demosite)
        
        print("pincode", pincode)
        print("city", city)
        print("state", state)
        print("country", country)
        print("address", address)
        print("lattitude", lattitude)
        print("longitude", longitude)

        print("data2nic", data2nic)
        print("nic_alert_email", nic_alert_email)
        print("data2sdc", data2sdc)
        print("sdc_alert_email", sdc_alert_email)
        print("data2ce", data2ce)
        print("ce_alert_email", ce_alert_email)
        print("data2wims", address)

        print("enc_key", enc_key)
        print("prv_key", prv_key)
        print("pub_key", pub_key)

        print("sinage", sinage)
        print("sms_alert", sms_alert)
        print("email_alert", email_alert)
        print("watsapp_alert", watsapp_alert)
        print("delay_hr", delay_hr)
        print("offline_hr", offline_hr)


        message = 'success'

        try:
            if(len(Site.objects.filter(site_id = site_id))):
                return JsonResponse({'message':'Site Id already registered with different station'})

            # new_user = UserProfile.objects.create(user=userObj,
            #                                     name=user_fullname,
            #                                     phone=user_contact,
            #                                     user_type=user_userType,
            #                                     demo_user=demoUser,
            #                                     address=user_address,
            #                                     zipcode=user_pincode,
            #                                     state=user_state,
            #                                     city=user_city,
            #                                     country=user_country
            #                                     )
        except Exception as err:
            message = str(err)

        print('message >>> ',message)

        return JsonResponse({'message':message})

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




