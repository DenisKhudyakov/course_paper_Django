from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from mailservice.forms import ClientForm, MailingSettingsForm, MessageForm
from mailservice.models import Client, MailingSettings, Message, Logs
from users.utils import UserRequiredMixin


class HomePageView(TemplateView):
    template_name = "mailservice/base.html"


class ClientListView(LoginRequiredMixin, ListView):
    """Список клиентов"""

    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Просмотр одного клиента"""

    model = Client


class ClientCreateView(LoginRequiredMixin, UserRequiredMixin, CreateView):
    """Класс создания клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("mailservice:clients")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("mailservice:clients")


class ClientDeleteView(LoginRequiredMixin, UserRequiredMixin, DeleteView):
    """Класс удаления клиента"""

    model = Client
    success_url = "mailservice:clients"


class MailingSettingsListView(LoginRequiredMixin, ListView):
    """Класс отображения рассылок"""

    model = MailingSettings


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    """Класс отображения отдельной рассылки"""

    model = MailingSettings


class MailingSettingsCreateView(LoginRequiredMixin, UserRequiredMixin, CreateView):
    """Класс создания рассылки"""

    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailservice:settings")


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    """Класс обновления рассылки"""

    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailservice:settings")


class MailingSettingsDeleteView(LoginRequiredMixin, UserRequiredMixin, DeleteView):
    """Класс удаления рассылки"""

    model = MailingSettings
    success_url = reverse_lazy("mailservice:settings")


class MessageListView(ListView):
    """Класс отображения сообщения"""

    model = Message


class MessageDetailView(DetailView):
    """Класс отображения отдельного сообщения"""

    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс создания сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailservice:messages")


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailservice:messages")


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления сообщения"""

    model = Message
    success_url = reverse_lazy("mailservice:messages")


class LogsCreateView(CreateView):
    """Класс создания логов"""
    model = Logs

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class LogsListView(LoginRequiredMixin, ListView):
    """Класс отображения логов"""
    model = Logs
    def get_queryset(self):
        return Logs.objects.filter(user=self.request.user)