from django.db import models
from django.contrib.auth.models import User, Permission
import uuid
import django
from monitoring_app.models import Site


PERMISSIONS = ()
USER_CHOICES = (
('1', 'Active User'),
('2', 'Staff User'),
('3', 'Super Admin'),
)
# user profile model
class UserProfile(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # site = models.ManyToManyField(Site, default=None)
    # email = models.EmailField(max_length=60, default=None, null=True,unique=True)
    name = models.CharField(max_length=60, null=False, verbose_name='Name')
    phone = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True,verbose_name='Created On')
    # last_login = models.DateTimeField(auto_now_add=True, blank=True)
    last_pwd_updated = models.DateField(auto_now=True,verbose_name='Password Updated On')
    # TODO: remove old image file if updated new logo
    # logo = models.ImageField(upload_to='logos/',default=settings.DEFAULT_LOGO)
    user_type = models.CharField(max_length=20, null=False, choices=USER_CHOICES)

    # for customers
    demo_user = models.BooleanField(default=False)
    address = models.TextField(default=None, null=True)
    zipcode = models.IntegerField(default=None, null=True)
    state = models.CharField(max_length=80, null=True)
    city = models.CharField(max_length=80, null=True)
    country = models.CharField(max_length=80, default='India', editable=False)
    # user permissions
    permissions = models.ManyToManyField(Permission, default=None)

    added_by = models.CharField(default='', verbose_name='Added By',max_length=120,blank=True)
    last_updated_by = models.CharField(default='', verbose_name='Last Updated By',max_length=120,blank=True)
    created_at = models.DateTimeField(blank=True,default=django.utils.timezone.now)
