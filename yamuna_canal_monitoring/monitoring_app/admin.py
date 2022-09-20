from django.contrib import admin
from monitoring_app.models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "site_id", "prefix", "to_sdc", "to_nic", "to_ce_okhla", "to_wims", "site_added_by", "created_at" ,"last_updated_at")
    list_filter = ('to_sdc', 'to_nic', 'to_ce_okhla', 'site_added_by')

admin.site.register(Site, SiteAdmin)