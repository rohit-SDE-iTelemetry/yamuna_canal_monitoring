from django.contrib import admin
from auth_app.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("uuid", "user", "email", "name", "phone", "last_login", "user_type")

admin.site.register(UserProfile, UserProfileAdmin)