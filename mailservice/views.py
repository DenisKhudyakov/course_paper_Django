from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from mailservice.models import Client


class HomePageView(TemplateView):
    template_name = 'mailservice/base.html'


class ClientListView(ListView):
    """Список клиентов"""
    model = Client


