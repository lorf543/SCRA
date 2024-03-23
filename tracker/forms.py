from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    status_notes = forms.CharField(
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
        
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['account_number'].label = "Acc number"
 
        
    
        

