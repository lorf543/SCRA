from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from simple_history.models import HistoricalRecords


from .utility import *
from datetime import datetime, timedelta

# Create your models here.

class Customer_info(models.Model):
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    

class Account(models.Model):
        # ___________________Basic_info______________________________________
    account_number = models.CharField(max_length=50, blank=True, null=True)
    loan_type = models.CharField(
        max_length=50, choices=LOAN_TYPE, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_last_name = models.CharField(max_length=50, blank=True, null=True)
    open_state = models.CharField(
        max_length=50, choices=ESTADOS_UNIDOS, blank=True, null=True)
    acc_status = models.CharField(max_length=50, choices=ACCOUNT_STATUS)
    date_request = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    method_notification = models.CharField(
        max_length=50, choices=METHOD_NOTIFICATION)
    date_open_acc = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    military_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    qualify = models.BooleanField(blank=True, null=True, default=False)
    status_notes = models.TextField(blank=True, null=True)
    veteran = models.BooleanField(default=False, blank=True, null=True)

    #_____________________________More Info Letter_______________________________
    first_review = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='first_review_candidates', blank=True, null=True)
    date_mil = models.DateField(blank=True, null=True)
    date_alert_dl = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
        #_____________________________Denial Letter_______________________________
    second_review = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='second_review_candidates', blank=True, null=True)
    danial_date = models.DateField(blank=True, null=True)
    denial_note = models.TextField(blank=True, null=True)
    denial_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='costumer_dl',null=True, blank = True)
    
        # _______________________Approved_Info________________
    amount_refund = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    the_way_refund = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    date_refund = models.DateField(blank=True, null=True)
    where_fees = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    where_waived = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    waive_interest = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    Interest_Rate = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    Fees = models.CharField(max_length=50, blank=True, null=True,default="N/A")
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by',null=True, blank = True)
    approved_date = models.DateField(null=True, blank = True)
    
    created = models.DateField(auto_now_add=True, null=True, blank = True)
    updated = models.DateField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='costumer_add', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='costumer_update',null=True, blank = True)

    #_________________________________Pending_info______________________
    pending = models.CharField(max_length=50,choices=PENDING,null=True, blank=True)
    reason = models.CharField(max_length=50,null=True, blank=True)
    
    pending_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pending_add', null=True, blank = True)
    pending_date = models.DateField(null=True, blank=True)
    pending_note = models.TextField(null=True, blank=True)

    resolve_note = models.TextField(null=True, blank=True)
    resolve_date = models.DateField(null=True, blank=True)
    resolve_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resolve_add', null=True, blank = True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Customer'
        
    def __str__(self):
        return self.customer_name
    
    @property
    def f_date(self):#format the date 
        return self.military_date.strftime('%m/%d/%Y')
    
    def save(self, *args, **kwargs):
        #self._state.adding
        
        if self.military_date == None:
            self.qualify = False
            self.approved_by = None
            self.status_notes = (
                f"SCRA account review. We have checked the military date N/A and the open account date "
                f"{self.date_open_acc.strftime('%m/%d/%Y')}. The account does not qualify for SCRA benefits. "
                f"Issuing a more information letter."
            )
        # special states
        elif self.military_date and self.open_state == "Ohio":
            self.qualify = True
            self.approved_date = timezone.now().date()
            self.status_notes = f"SCRA account review Ohio account {self.military_date.strftime('%m/%d/%Y')} open account {self.date_open_acc.strftime('%m/%d/%Y')}"
           
        elif self.military_date and self.open_state == "Pennsylvania" and self.loan_type == "RISA":
            days_difference = (self.date_open_acc - self.military_date).days
            if days_difference > 30:
                self.qualify = False
                self.approved_date = timezone.now().date()
                self.status_notes = (
                                    f"SCRA account review Pennsylvania account {self.military_date.strftime('%m/%d/%Y')} "
                                    f"open account {self.date_open_acc.strftime('%m/%d/%Y')}")
            else:
                self.qualify = False
                self.approved_by = None
                self.status_notes = f""" SCRA account review. we have check form military date N/A and the open account date {self.date_open_acc.strftime('%m/%d/%Y')}. account does not qualify for SCRA benefits. issuing a more information letter.
                """

        elif self.military_date >= self.date_open_acc:
            self.qualify = True
            self.approved_date = timezone.now().date()
            self.status_notes =  f"""SCRA account review Approval note. we have check form military date {self.military_date.strftime('%m/%d/%Y')}. and the open account date {self.date_open_acc.strftime('%m/%d/%Y')}. Account qualify for SCRA benefits. issuing a Approval letter."""

        else:
            self.qualify = False
            self.approved_by = None
            self.status_notes = f""" SCRA account review. we have check form military date N/A and the open account date {self.date_open_acc.strftime('%m/%d/%Y')}. account does not qualify for SCRA benefits. issuing a more information letter.
                """
        
            
        super(Account, self).save(*args, **kwargs)  
    
@receiver(pre_save, sender=Account)
def set_letter_dates(sender, instance, *args, **kwargs):
    instance.date_mil = datetime.today()
    instance. date_alert_dl = instance.date_mil + timedelta(days=30)
    
    pre_save.connect(set_letter_dates, sender=Account)
    
    
class Address(models.Model):
    customer = models.ForeignKey(Account, related_name="customer_address", on_delete=models.CASCADE,null=True, blank = True)
    street = models.CharField(max_length=150, null=True, blank = True)
    street2 = models.CharField(max_length=150, null=True, blank = True)
    city = models.CharField(max_length=150, null=True, blank = True)
    state = models.CharField(max_length=150, choices=ESTADOS_UNIDOS ,null=True, blank = True)
    zipcode = models.CharField(max_length=25, null=True, blank = True)
    return_type = models.CharField(max_length=50, choices=RETURN_TYPE, blank=True, null=True)
    return_note = models.TextField(null=True, blank=True)
    address_status = models.CharField(max_length=50, choices=ADDRESS_STATUS,blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True, null=True, blank = True)
    updated = models.DateTimeField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_add', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_update',null=True, blank = True)
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Customer Address'
        ordering = ['-created']
        
    def __str__(self):
        return self.customer.customer_name +" "+ self.street
    
class Duplicates(models.Model):
    customer = models.ForeignKey(Account, related_name="customer_Duplicates", on_delete=models.CASCADE,null=True, blank = True)
    duplicate_note = models.TextField(null=True, blank=True)
    veteran = models.BooleanField(default=False, blank=True, null=True)
    
    created = models.DateField(auto_now_add=True, null=True, blank = True)
    updated = models.DateField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Duplicates_add', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Duplicates_update',null=True, blank = True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.customer.customer_name
    
    class meta:
        verbose_name_plural = 'Duplicates'
        ordering = ['created']