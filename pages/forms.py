from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            }),
        }
