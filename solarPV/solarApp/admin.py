from django.contrib import admin
from solarApp.models import *
# class transferID(admin.ModelAdmin):
#     pass
# admin.site.register(transferID, transferID)
# Register your models here.
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(TestStandard)
admin.site.register(Certificate)

