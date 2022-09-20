from django.db import models
import uuid
import django


# site model
class Site(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=120)
    name = models.CharField(max_length=100, verbose_name='Station')
    site_id = models.CharField(max_length=80, verbose_name='StationID/SiteID',default=None, null=True)
    key = models.TextField(max_length=1000, default=None, null=True,verbose_name='Key or Token', blank=True)
    prefix = models.CharField(max_length=64, unique=True,verbose_name='site Prefix')
    version = models.CharField(max_length=10, default='ver_1.0',verbose_name='Software Version',blank=True)

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
    user_email = models.TextField(max_length=255, default=None, null=True,verbose_name='Customer Alert Email',blank=True)
    user_phone = models.TextField(max_length=255, default=None, null=True,verbose_name='Customer Alert Contact',blank=True)

    #  data sent options
    to_sdc = models.BooleanField(default=False,help_text='send data to SDC',verbose_name='To SDC',blank=True)
    to_nic = models.BooleanField(default=False,help_text='send data to NIC',verbose_name='To NIC',blank=True)
    to_ce_okhla = models.BooleanField(default=False,help_text='send data to CE Okhla',verbose_name='To CE Okhla',blank=True)
    to_wims= models.BooleanField(default=False,help_text='send data to WIMS',verbose_name='To WIMS',blank=True)

    enable_led = models.BooleanField(default=False, null=False,verbose_name='Led Display')
    # default: 4 hours
    hours2delay = models.IntegerField(default=4, null=False,verbose_name='set Delay in N mins')
    # default: 48 hours
    hours2offline = models.IntegerField(default=48,null=False,verbose_name='set Offline in N mins')

    # alerts
    enable_email_alerts = models.BooleanField(default=False,verbose_name='Email Alerts',help_text='send email alerts',blank=True)
    enable_sms_alerts = models.BooleanField(default=False,verbose_name='SMS Alerts',help_text='send sms alerts',blank=True)
    max_email_alerts = models.CharField(max_length=100, null=True)
    max_sms_alerts = models.CharField(max_length=100, null=True)

    calibration = models.BooleanField(default=False,help_text='calibration enabled')

    site_added_by = models.CharField(default='', verbose_name='Added By',max_length=120,blank=True)
    last_updated_by = models.CharField(default='', verbose_name='Last Updated By',max_length=120,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    last_updated_at = models.DateTimeField(default=django.utils.timezone.now,editable=False)


