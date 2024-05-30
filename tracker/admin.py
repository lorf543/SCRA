from django.contrib import admin

from .models import Account,Address,Duplicates
# Register your models here.



class CustomerAdmind(admin.ModelAdmin):
    fieldsets = [
        ("Loan info",{"fields":(("loan_type","account_number"),("customer_name","open_state"),("acc_status",
        "date_request","method_notification",),"date_open_acc","military_date","status_notes","added_by")}),
        
        ("Approval info",{"fields":("qualify",("the_way_refund","where_fees"),("where_waived","waive_interest"),("Interest_Rate","Fees"),)}),
        
        ("More information latter",{"fields":("first_review","date_mil")}),

        ("Second information latter",{"fields":("second_review","danial_date","denial_note","date_alert_dl",)}),

        ("Pending Information",{"fields":(("pending","reason",),"pending_note","resolve_note",("resolve_date","pending_date"))})
]
admin.site.register(Account,CustomerAdmind)


admin.site.register(Address)
admin.site.register(Duplicates)
