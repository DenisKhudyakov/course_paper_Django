from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from mailservice.models import Client, MailingSettings, Message


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
    """Класс удаления клиента"""
    model = Client
    success_url = 'mailservice:clients'


class MailingSettingsListView(ListView):
    """Класс отображения рассылок"""
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    """Класс отображения отдельной рассылки"""
    model = MailingSettings
    

class MailingSettingsCreateView(CreateView):
    """Класс создания рассылки"""
    model = MailingSettings
    fields = '__all__'
    success_url = reverse_lazy('mailservice:settings')


class MailingSettingsUpdateView(UpdateView):
    """Класс обновления рассылки"""
    model = MailingSettings
    fields = '__all__'
    success_url = reverse_lazy('mailservice:settings')


class MailingSettingsDeleteView(DeleteView):
    """Класс удаления рассылки"""
    model = MailingSettings
    success_url = reverse_lazy('mailservice:settings')


class MessageListView(ListView):
    """Класс отображения сообщения"""
    model = Message


class MessageDetailView(DetailView):
    """Класс отображения отдельного сообщения"""
    model = Message


class MessageCreateView(CreateView):
    """Класс создания сообщения"""
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailservice:messages')


class MessageUpdateView(UpdateView):
    """Класс редактирования сообщения"""
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailservice:messages')


class MessageDeleteView(DeleteView):
    """Класс удаления сообщения"""
    model = Message
    success_url = reverse_lazy('mailservice:messages')
