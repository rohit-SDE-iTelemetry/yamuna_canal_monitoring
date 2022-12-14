from monitoring_app.models import Reading2022
from datetime import datetime, timedelta

# check last reading for status check
def check_site_status(site_obj):
    print('site_obj >>>> ',site_obj)
    status = ''
    last_record = Reading2022.objects.filter(site = site_obj.site).last()
    if(last_record):
        status = 'Live'
    else:
        status = 'No Record Availabe'
    
    return status
