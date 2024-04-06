from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from mailservice.models import Client


class HomePageView(TemplateView):
    template_name = 'mailservice/base.html'


class ClientListView(ListView):
    """Список клиентов"""
    model = Client


class ClientDetailView(DetailView):
    """Просмотр одного клиента"""
    model = Client


class ClientCreateView(CreateView):
    """Класс создания клиента"""
    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse('mailservice:clients')


class ClientUpdateView(UpdateView):
    """Класс редактирования клиента"""
    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse('mailservice:clients')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = 'mailservice:clients'



