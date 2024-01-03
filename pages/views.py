from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Index page data


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactFormView(SuccessMessageMixin, CreateView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_message = "Your message has been successfully sent. We will get back to you soon."

    def get_success_url(self):
        return reverse("pages:contact")
