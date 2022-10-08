from django.contrib import admin
from auth_app.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("uuid", "user", "name", "phone", "user_type")

admin.site.register(UserProfile, UserProfileAdmin)