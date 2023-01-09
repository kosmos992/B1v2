from django.contrib import admin

# Register your models here.
from mapapp.models import Cctv, PoliceOffice
from static.import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class CctvAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class PoliceOfficeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Cctv, CctvAdmin)

admin.site.register(PoliceOffice, PoliceOfficeAdmin)