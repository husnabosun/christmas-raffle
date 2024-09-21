from django.contrib import admin
from .models import ApplicantProfile
from import_export.admin import ImportExportModelAdmin


admin.site.register(ApplicantProfile, ImportExportModelAdmin)
