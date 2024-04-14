from django.db import models
from django.contrib.auth.models import User

from tracker.models import Account
from tracker.models import NOTIFICATION

# Create your models here.

class Inbox(models.Model):
    customer = models.ForeignKey(Account, related_name='customer_inbox', on_delete=models.CASCADE)
    method_notification = models.CharField(max_length=50, choices=NOTIFICATION)
    date_received = models.DateField(null=True, blank= True)
    email_received = models.TextField()
    email_sent = models.TextField(null=True, blank=True)
    email_sent_date = models.DateField(null=True, blank=True)
    valid = models.BooleanField(null=True, blank= True)
        
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(null=True, blank = True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox_add', null=True, blank = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox_update',null=True, blank = True)
    
    def __str__(self):
        return self.customer.customer_name
    