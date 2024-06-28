from .models import Notes
from django import forms

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = "__all__"
