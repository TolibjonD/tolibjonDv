from django.contrib import admin
from .models import VisitorsInformation


# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    search_fields = ["device_pr"]
    list_filter = ["device_pr", "ip", "created_at"]


admin.site.register(VisitorsInformation, CustomAdmin)
