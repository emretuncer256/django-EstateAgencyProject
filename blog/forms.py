from django import forms
from django.forms import ModelForm

from .models import Comment


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "website", "message", "blog", "parent")

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg form-control-a",
                "placeholder": "Name *"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control form-control-lg form-control-a",
                "placeholder": "Email *"
            }),
            "website": forms.TextInput(attrs={
                "class": "form-control form-control-lg form-control-a",
                "placeholder": "Website",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Comment *",
                "rows": 8,
                "cols": 45
            }),
            "parent": forms.HiddenInput(),
            "blog": forms.HiddenInput()
        }
