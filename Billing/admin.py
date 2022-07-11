from django.contrib import admin
import csv
from Billing.models import Cust_Detals
from django.http import HttpResponse
from django.db.models import F

# Register your models here.
def Export_Records(modeladmin,requeset,queryset):
    response =HttpResponse(content_type='text/csv')
    response['Content Description']='Attachment; filename="Records.csv"'
    writer = csv.writer(response)
    writer.writerow(['id','SR_No','Cust_name','Mobile','WeightK','WeightG'])
    Cust_Detals=queryset.values_list('id','SR_No','Cust_name','Mobile','WeightK','WeightG')
    for s in Cust_Detals:
        writer.writerow(s)
    return response
Export_Records.short_description="Export To CSV"

class cust_DetailsAdmin(admin.ModelAdmin):
    list_display=('id','SR_No','Cust_name','Mobile','WeightK','WeightG') 
    actions=[Export_Records]
admin.site.register(Cust_Detals,cust_DetailsAdmin)