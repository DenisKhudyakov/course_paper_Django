from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView, View
from django.contrib.auth.views import LogoutView as BaseLogoutView
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserLogin(LoginView):
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    pass


class UserCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = ("users/user_form.html")
    success_url = reverse_lazy("users:login")
    success_message = "Вы успешно зарегистрировались на сайте"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация на сайте"
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # не активируем пользователя
        user.save()
        # Функционал для отправки письма на почту
        token = default_token_generator.make_token(user)  # создание токена
        user.token = token
        user.save()
        uid = urlsafe_base64_encode(force_str(user.pk).encode())  # кодирование id пользователя
        activation_url = reverse_lazy(
            "users:activation", kwargs={"uidb64": uid, "token": token}
        )
        activation_url = self.request.build_absolute_uri(activation_url)
        send_mail(
            message=render_to_string("users/confirm_email.html", {"activation_url": activation_url}),  # сообщение
            from_email=EMAIL_HOST_USER,  # отправитель
            recipient_list=[user.email],  # получатель
            fail_silently=False,  # не пытаемся отправить письмо
        )

        return super().form_valid(form)


def activation(request, uidb64, token):
    """Подтверждение почты пользователя"""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("users:login")
    else:
        return redirect("users:email_confirmation_failed")