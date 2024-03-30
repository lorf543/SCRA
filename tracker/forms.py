from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    status_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows":"5","cols": "15"}))
    

    account_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'hx-post':'/check-customer/',
            'hx-swap':'outerhtml',
            'hx-triger':'keyup delay:2s',
            'hx-target':'#customer_error'
        })
    )    

    class Meta:
        model = Customer
        
        fields = "__all__"
        
        labels = {
            'amount_refund':'Amount Refund',
            'date_open_acc':'Date Open Account',
            'the_way_refund':'Way the refund was made',
        }
        widgets = {
            'date_refund': forms.DateInput(attrs={'type':'date',}),
            'date_open_acc': forms.DateInput(attrs={'type':'date',}),
            'military_date': forms.DateInput(attrs={'type':'date',}),
            'date_request': forms.DateInput(attrs={'type':'date',}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].label = "Acc number"
 
        
    
        

