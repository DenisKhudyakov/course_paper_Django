from django import forms

from mailservice.models import Client, Message, MailingSettings


class StyleMixinForm:
    """Класс стилизации формы"""
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = f'Введите {field_name}'


class ClientForm(forms.ModelForm):
    """Класс формы клиента"""
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(forms.ModelForm):
    """Класс формы сообщения"""
    class Meta:
        model = Message
        fields = '__all__'


class MailingSettingsForm(StyleMixinForm, forms.ModelForm):
    """Класс формы рассылки"""
    class Meta:
        model = MailingSettings
        fields = '__all__'