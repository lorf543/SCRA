from django import forms

from .models import Account,Address


class CustomerForm(forms.ModelForm):
    status_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows":"5","cols": "15"}))
    
    date_refund = forms.DateField(
        required=False
    )

    account_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'hx-post':'/check-customer/',
            'hx-swap':'outerhtml',
            'hx-triger':'keyup delay:2s',
            'hx-target':'#customer_error'
        })
    )    

    class Meta:
        model = Account
        
        fields = "__all__"
        
        labels = {
            'amount_refund':'Amount Refund',
            'date_open_acc':'Date Open Account',
            'the_way_refund':'Way the refund was made',
            'danial_date':'Denial date',
            'method_notification':'Notification'
        }
        widgets = {
            'date_refund': forms.DateInput(attrs={'type':'date',}),
            'date_open_acc': forms.DateInput(attrs={'type':'date',}),
            'military_date': forms.DateInput(attrs={'type':'date',}),
            'date_request': forms.DateInput(attrs={'type':'date',}),
            'danial_date': forms.DateInput(attrs={'type':'date',}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].label = "Acc number"
 
      
class AddressForm(forms.ModelForm):
    
    return_note = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"rows":5, "cols":5,"placeholder":"testing carajoasda sd "}))
        
    class Meta:
        model = Address
        fields = ['street','street2','city','state','zipcode',
                  'address_status','return_note','return_type']
        
    


