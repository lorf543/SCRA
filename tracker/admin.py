from django.contrib import admin

from .models import Customer
# Register your models here.



class CustomerAdmind(admin.ModelAdmin):
    fieldsets = [
        ("Loan info",{"fields":("loan_type","account_number","customer_name","open_state","acc_status",
        "date_request","method_notification","date_open_acc","military_date","status_notes")}),
        
        ("Approval info",{"fields":("qualify","the_way_refund","date_refund","where_fees","where_waived","waive_interest",)})
]
    
    
admin.site.register(Customer,CustomerAdmind)