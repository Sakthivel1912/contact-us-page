from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'maxlength': 100}))
    message = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 500}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
