from django import forms
from .models import Account,Address, Duplicates

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

def accNumber (value):
    patron = r'^[0-9/-]*$' 
    if not re.match(patron, value):
        raise forms.ValidationError('Only numbers allow')
    
class DuplicatesForm(forms.ModelForm):
    class Meta:
        model = Duplicates
        fields = ["duplicate_note",]
    


class CustomerForm(forms.ModelForm):

    status_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows":"5","cols": "15"}))
    

    customer_name = forms.CharField(
        required=True,
        validators=[
        RegexValidator('^[a-zA-ZÀ-ÿ\s]*$',
        message='Only letters allow here')
        ]
    )

    customer_last_name = forms.CharField(
        required=True,
        validators=[
        RegexValidator('^[a-zA-ZÀ-ÿ\s]*$',
        message='Only letters allow here')
        ]
    )

    account_number = forms.CharField(
        required=True,
        validators=[accNumber],
        widget=forms.TextInput(attrs={
            'hx-post':'/check-customer/',
            'hx-swap':'outerhtml',
            'hx-triger':'keyup delay:2s',
            'hx-target':'#customer_error'
        })
    )

    veteran = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={}
        )
    )

    class Meta:
        model = Account
        
        fields = [ 'customer_name','customer_last_name','account_number','open_state',
                    'loan_type','open_state','acc_status','date_request',
                    'method_notification','date_open_acc','military_date',
                    'veteran','pending','reason','pending_by','pending_date',
                    'danial_date','denial_note','pending_note','resolve_note',
                    'resolve_date','amount_refund','the_way_refund','date_refund',
                    'where_fees','Interest_Rate','Fees'
                ]
        
        labels = {
            'amount_refund':'Amount Refund',
            'date_open_acc':'Date Open Account',
            'the_way_refund':'Way the refund was made',
            'danial_date':'Denial date',
            'method_notification':'Notification',
        }
        widgets = {
            'date_open_acc': forms.DateInput(attrs={'type':'date',}),
            'military_date': forms.DateInput(attrs={'type':'date',}),
            'date_request': forms.DateInput(attrs={'type':'date',}),
            'danial_date': forms.DateInput(attrs={'type':'date',}),
            'date_refund': forms.DateInput(attrs={'type':'date',}),
            'pending_date': forms.DateInput(attrs={'type':'date',}),
            'resolve_date': forms.DateInput(attrs={'type':'date',}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        #self.fields['account_number'].label = "Acc number"
        self.fields['date_open_acc'].required = True
        self.fields['date_request'].required = True
        self.fields['date_request'].required = True
        self.fields['open_state'].required = True
        self.fields['loan_type'].required = True
 
      
class AddressForm(forms.ModelForm):
    
    return_note = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"rows":5, "cols":5,"placeholder":":3"}))
        
    class Meta:
        model = Address
        fields = ['street','street2','city','state','zipcode',
                  'address_status','return_note','return_type']
        
    


