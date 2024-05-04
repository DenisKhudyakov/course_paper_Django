from django import forms

from mailservice.models import Client, Message, MailingSettings


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        fields = '__all__'