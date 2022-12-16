from monitoring_app.models import Reading2022, SiteInfo, Site
from datetime import datetime, timedelta, timezone

# check last reading for status check
def check_site_status(site_obj):
    last_record = Reading2022.objects.filter(site = site_obj.site).last()
    if(last_record):
        hours = get_tdifference(datetime.now(timezone.utc),last_record.timestamp)
        if(hours >= 0 and hours < site_obj.hours2delay):
            status = 'Live'
        elif(hours < 0):
            status = 'Live'
        elif(hours >= site_obj.hours2delay and hours < site_obj.hours2offline):
            status = 'Delay'
        elif(hours >= site_obj.hours2offline and hours < site_obj.hours2offline):
            status = 'No Record Available'
        else:
            status = 'Disabled'
    else:
        status = 'No Record Available'
    
    site_obj.site_status = status
    site_obj.save()
    site_obj.site.site_status = status
    site_obj.save()
    return status


# get timedifference in hours
def get_tdifference(current,reading_tstamp):
    difference = current - reading_tstamp
    hours = difference.total_seconds() / 3600
    return hours

# get details of status wise site
def site_details(context_dict):
    context_dict['sites'] = SiteInfo.objects.all()
    context_dict['live_sites'] = Site.objects.filter(site_status='Live').count()
    context_dict['delay_sites'] = Site.objects.filter(site_status='Delay').count()
    context_dict['offline_sites'] = Site.objects.filter(site_status='Offline').count()
    context_dict['disabled_sites'] = Site.objects.filter(site_status='Disabled').count()
    context_dict['nat_sites'] = Site.objects.filter(site_status='No Record Availabe').count()
    context_dict['last_reading'] = Reading2022.objects.latest('timestamp')
    return context_dict
