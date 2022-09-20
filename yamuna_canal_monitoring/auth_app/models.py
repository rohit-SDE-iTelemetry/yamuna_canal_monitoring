from django.db import models
from django.contrib.auth.models import User, Permission
import uuid

from monitoring_app.models import Site

# user profile model
class UserProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
