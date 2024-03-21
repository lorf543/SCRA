from django.db import models
from .utility import *

# Create your models here.

class Customer(models.Model):
        # ___________________Basic_info______________________________________
    account_number = models.CharField(max_length=50, blank=True, null=True)
    loan_type = models.CharField(
        max_length=50, choices=LOAN_TYPE, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
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
    qualify = models.BooleanField()
    status_notes = models.TextField(blank=True, null=True)
        # _______________________Approved_Info________________
    amount_refund = models.CharField(max_length=50, blank=True, null=True)
    the_way_refund = models.CharField(max_length=50, blank=True, null=True)
    date_refund = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    where_fees = models.CharField(max_length=50, blank=True, null=True)
    where_waived = models.CharField(max_length=50, blank=True, null=True)
    waive_interest = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self):
        return self.customer_name
    
    
    class Meta:
        verbose_name = 'Customer'
    
    