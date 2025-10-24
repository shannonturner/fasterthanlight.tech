from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import ContactForm
from .models import Submission

import logging

log = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class PostContactView(TemplateView):
    template_name = "contact.html"

class ServicesView(CreateView):

    model = Submission
    form_class = ContactForm

    template_name = "services.html"
    success_url = "/contact"

    def form_valid(self, form):

        try:
            form.send_email()
        except Exception:
            log.critical("Failed to form.send_email(), be sure to check submission for followup!")

        return super().form_valid(form)

class ActionKitView(TemplateView):
    template_name = "actionkit.html"

class DeliverabilityView(TemplateView):
    template_name = "deliverability.html"

class TrainingView(TemplateView):
    template_name = "training.html"
