from django.contrib import admin
from monitoring_app.models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "site_id", "prefix", "to_sdc", "to_nic", "to_ce_okhla", "to_wims")
    list_filter = ('to_sdc', 'to_nic', 'to_ce_okhla')

admin.site.register(Site, SiteAdmin)