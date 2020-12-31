from django import forms
from .models import Contact


# contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name',
                  'subject',
                  'email',
                  'message']

    full_name = forms.CharField(
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'class': 'border-black rounded-0',
            'placeholder': 'Full Name'
        })
    )

    subject = forms.CharField(
        required=True,
        label='Subject',
        widget=forms.TextInput(attrs={
            'class': 'border-black rounded-0',
            'placeholder': 'Subject'
        })
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'border-black rounded-0',
            'placeholder': 'Email Address'
        })
    )

    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'border-black rounded-0',
            'placeholder': 'Please enter your message'
        })
    )
