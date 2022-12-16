from django.db import models
import uuid
import django

# category master model
class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=120)
    category_name = models.CharField(max_length=100, verbose_name='Category Name')
    category_slug = models.CharField(max_length=100, verbose_name='Category Slug')
    site_added_by = models.CharField(default='', verbose_name='Added By',max_length=120,blank=True)
    last_updated_by = models.CharField(default='', verbose_name='Last Updated By',max_length=120,blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    last_updated_at = models.DateTimeField(default=django.utils.timezone.now)


# site model
class Site(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=120)
    name = models.CharField(max_length=100, verbose_name='Station')
    site_id = models.CharField(max_length=80, unique=True,verbose_name='StationID/SiteID', default=None, null=True)
    key = models.TextField(max_length=1000, default=None, null=True,verbose_name='Key or Token', blank=True)
    prefix = models.CharField(max_length=64, unique=True, verbose_name='site Prefix')
    site_status = models.CharField(max_length=20, verbose_name='site status', default='NAT')
    version = models.CharField(max_length=10, default='ver_1.0',verbose_name='Software Version',blank=True)
    site_category = models.ForeignKey(Category, blank=True, null=True,verbose_name="Site Category", on_delete=models.CASCADE)

    # Address details of the Site
    address = models.TextField(default=None, null=True, blank=True)
    zipcode = models.IntegerField(default=None, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=15, max_digits=20,null=True,blank=True)
    latitude = models.DecimalField(decimal_places=15, max_digits=20, null=True,blank=True)
    state = models.CharField(max_length=80, null=True)
    city = models.CharField(max_length=80, null=True)
    district = models.CharField(max_length=80, null=True)
    country = models.CharField(max_length=80, default='India', editable=False,
                               blank=True)
    # emails/phone of customer
    user_email = models.TextField(max_length=255, unique=True, default=None, null=True,verbose_name='Customer Alert Email',blank=True)
    user_phone = models.TextField(max_length=255, unique=True, default=None, null=True,verbose_name='Customer Alert Contact',blank=True)

    #  data sent options
    to_sdc = models.BooleanField(default=False,help_text='send data to SDC',verbose_name='To SDC',blank=True)
    to_nic = models.BooleanField(default=False,help_text='send data to NIC',verbose_name='To NIC',blank=True)
    to_ce_okhla = models.BooleanField(default=False,help_text='send data to CE Okhla',verbose_name='To CE Okhla',blank=True)
    to_wims= models.BooleanField(default=False,help_text='send data to WIMS',verbose_name='To WIMS',blank=True)

    nic_alert_email = models.CharField(max_length=255, default='', null=True,verbose_name='NIC Alert Email',blank=True)
    sdc_alert_email = models.CharField(max_length=255, default='', null=True,verbose_name='SDC Alert Email',blank=True)
    ce_okhla_alert_email = models.CharField(max_length=255, default='', null=True,verbose_name='CE Okhla Alert Email',blank=True)

    enable_led = models.BooleanField(default=False, null=False,verbose_name='Led Display')
    # default: 4 hours
    hours2delay = models.IntegerField(default=4, null=False,verbose_name='set Delay in N mins')
    # default: 48 hours
    hours2offline = models.IntegerField(default=48,null=False,verbose_name='set Offline in N mins')

    # alerts
    enable_email_alerts = models.BooleanField(default=False,verbose_name='Email Alerts',help_text='send email alerts',blank=True)
    enable_sms_alerts = models.BooleanField(default=False,verbose_name='SMS Alerts',help_text='send sms alerts',blank=True)
    enable_watsapp_alerts = models.BooleanField(default=False,verbose_name='Watsapp Alerts',help_text='send sms alerts',blank=True)
    max_email_alerts = models.CharField(max_length=100, null=True)
    max_sms_alerts = models.CharField(max_length=100, null=True)

    calibration = models.BooleanField(default=False,help_text='calibration enabled')

    site_added_by = models.CharField(default='', verbose_name='Added By',max_length=120,blank=True)
    last_updated_by = models.CharField(default='', verbose_name='Last Updated By',max_length=120,blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    last_updated_at = models.DateTimeField(default=django.utils.timezone.now)



# parameter master model
class Parameter(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=120)
    parameter_name = models.CharField(max_length=100, verbose_name='Parameter Name')
    parameter_slug = models.CharField(max_length=100, verbose_name='Parameter Slug')
    site_added_by = models.CharField(default='', verbose_name='Added By',max_length=120,blank=True)
    last_updated_by = models.CharField(default='', verbose_name='Last Updated By',max_length=120,blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    last_updated_at = models.DateTimeField(default=django.utils.timezone.now)



# site readings model
class Reading2022(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True)
    site = models.ForeignKey(Site, null=False,related_name='readings2022',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True, null=False)
    readings = models.TextField(max_length=999, blank=True)

    class Meta:
        unique_together = (('site', 'timestamp'),)



# this holds all info site specific
class SiteInfo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, max_length=120)
    site = models.OneToOneField(Site,on_delete=models.CASCADE,primary_key=True)
    last_seen = models.DateTimeField(verbose_name='Last Seen',blank=True,null=True)
    # mail_interval = models.IntegerField(default=12,null=True,verbose_name='Mail Alert Intervals')
    # sms_interval = models.IntegerField(default=12,null=True,verbose_name='SMS Alert Intervals')
    last_upload_info = models.TextField(max_length=256,blank=True,default='')
    readings = models.TextField(max_length=999, blank=True, null=True)
    file_info = models.TextField(default=None, null=True)
    # rename later
    nic_status = models.BooleanField(default=False,verbose_name='NIC Upload Status')
    sdc_status = models.BooleanField(default=False,verbose_name='SDC Upload Status')
    received_at = models.DateTimeField(blank=True,null=True)
    freq = models.CharField(max_length=256, blank=True,verbose_name='File Frequency')
    var5 = models.CharField(max_length=256, blank=True)
    site_status = models.CharField(max_length=20, verbose_name='site status', default='NAT')

