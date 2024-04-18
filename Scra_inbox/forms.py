from django import forms

from Scra_inbox.models import Inbox

from django_flatpickr.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    TimePickerInput,
)

from tracker.models import NOTIFICATION

class InboxForm(forms.ModelForm):
    
    email_received = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"rows":5, "cols":5,})
    )
    
    email_sent = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"rows":5, "cols":5})
    )
    
    method_notification = forms.ChoiceField(
        choices=NOTIFICATION,
        required=False,
        label='Notification',
        widget=forms.Select(attrs={})
    )
    date_received = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'End Date',"id":"test_id"}),
        required=True

    )
    
    email_sent_date = forms.DateField(
        required=False,
        localize=True,
        widget=forms.DateInput(attrs={"type":"date"})
    )



    
    class Meta:
        model = Inbox
        fields = ["method_notification","date_received",
                "email_received","email_sent","email_sent_date","valid"]
    
