from django.contrib import admin

from hospital.models import Doctor, Patient


# Register your models here
admin.site.register(Doctor)
admin.site.register(Patient)