from django.contrib import admin
from monitoring_app.models import Site,Parameter,Category,SiteInfo,Reading2022


class SiteAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "site_id", "prefix", "to_sdc", "to_nic", "to_ce_okhla", "to_wims")
    list_filter = ('to_sdc', 'to_nic', 'to_ce_okhla')
admin.site.register(Site, SiteAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("uuid", "category_name", "category_slug", "created_at", "last_updated_at")
admin.site.register(Category, CategoryAdmin)


class ParameterAdmin(admin.ModelAdmin):
    list_display = ("uuid", "parameter_name", "parameter_slug", "created_at", "last_updated_at")
admin.site.register(Parameter, ParameterAdmin)


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ("site", "last_seen", "last_upload_info", "readings", "file_info")
admin.site.register(SiteInfo, SiteInfoAdmin)


class Reading2022Admin(admin.ModelAdmin):
    list_display = ("uuid", "site", "timestamp", "readings")
admin.site.register(Reading2022, Reading2022Admin)