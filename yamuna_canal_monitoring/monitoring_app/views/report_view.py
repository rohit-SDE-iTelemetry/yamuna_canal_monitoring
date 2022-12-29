from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from monitoring_app.models import Site, Reading2022
from datetime import datetime

#########################################################################################################
# REPORT MODULE
#########################################################################################################
@login_required(login_url='/')
def report(request):
    if request.method == 'GET':
        context = {}
        sitesObj = Site.objects.all()
        context['site_obj'] = sitesObj
        return render(request,'reports/report.html',context)


@login_required(login_url='/')
def report_filter(request):
    if request.method == 'GET':
        data = []
        station_uuid = request.GET.get('station_uuid')
        from_dt = request.GET.get('from_dt')
        to_dt = request.GET.get('to_dt')

        print('station_uuid >>>> ',station_uuid)
        print('from_dt >>>> ',from_dt)
        print('to_dt >>>> ',to_dt)
        siteObj = Site.objects.get(uuid=station_uuid)
        readings = Reading2022.objects.filter(site = siteObj, timestamp__range=[from_dt, to_dt]).order_by('timestamp')
        print('readings >>>>> ',readings)
        param_array = []
        header_str = ''
        for read in readings:
            convert_lst = read.readings.replace('"','').split(",")
            context = {}
            for j in convert_lst:
                if(j.split('=>')[0].capitalize() not in param_array):
                    param_array.append(j.split('=>')[0].capitalize())
                context[j.split('=>')[0].capitalize()] = j.split('=>')[1]
            context['timestamp'] = datetime.strftime(read.timestamp,"%d-%b-%Y %H:%M:%S")
            data.append(context)
        
        print('data >>>> ',data)

        return JsonResponse({'data_record':data})



# def generate_table(header_array, table_data):
#     table_string = ''

#     return table_string