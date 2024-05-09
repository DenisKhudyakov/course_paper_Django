from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from mailservice.forms import StyleMixinForm


class UserRegisterForm(UserCreationForm, StyleMixinForm):
    """Класс формы регистрации пользователя"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserForm(UserChangeForm, StyleMixinForm):
    """Класс формы пользователя"""

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "telephone",
        )  # , 'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
