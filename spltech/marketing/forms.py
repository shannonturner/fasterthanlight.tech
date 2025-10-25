from django import forms
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Submission

import datetime

class ContactForm(forms.ModelForm):

    name = forms.CharField(
        label="What is your name?",
        widget=forms.TextInput(attrs={
            "class": "form-control m-2 fs-4",
            "placeholder": "Your name",
        }),
    )

    organization = forms.CharField(
        label="What organization or campaign are you with?",
        widget=forms.TextInput(attrs={
            "class": "form-control m-2 fs-4",
            "placeholder": "Interplanetary Society",
        }),
    )

    phone = forms.CharField(
        label="What is your phone number?",
        widget=forms.TextInput(attrs={
            "class": "form-control m-2 fs-4",
            "placeholder": "(202) 555-0000",
        }),
        required=False,
    )

    email = forms.CharField(
        label="What is your email?",
        widget=forms.TextInput(attrs={
            "class": "form-control m-2 fs-4",
            "placeholder": "me@example.com",
        }),
    )

    additional_info = forms.CharField(
        label="Anything else you'd like to add?",
        widget=forms.Textarea(attrs={
            "class": "form-control my-3 fs-5",
            "rows": 5,
        }),
        help_text="""Tell me a little about your goals,
            or anything that might be helpful for me
            to know when preparing for a discovery call with you.
        """,
        required=False,
    )

    class Meta:
        model = Submission
        fields = ["name", "organization", "phone", "email", "services", "additional_info"]
        widgets = {
            "services": forms.CheckboxSelectMultiple(attrs={"class": "m-3"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].label = "What services would you like to discuss?"

    def send_email(self):

        text_content = render_to_string(
            "email_contact.txt",
            context={"cleaned_data": self.cleaned_data},
        )
        html_content = render_to_string(
            "email_contact.html",
            context={"cleaned_data": self.cleaned_data},
        )

        msg = EmailMultiAlternatives(
            f"Received contact form submission from {self.cleaned_data['name']} with {self.cleaned_data['organization']} at {datetime.datetime.now().isoformat(timespec='seconds')}",
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_FORM_EMAIL_TO],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
