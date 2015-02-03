from django.contrib import admin
from dashboard.models import Patient, Immunization, ImmunizationRecord

admin.site.register(Patient)
admin.site.register(Immunization)
admin.site.register(ImmunizationRecord)

# Register your models here.
