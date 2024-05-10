from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView, View

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import CustomUser


class UserLogin(LoginView):
    template_name = 'users/login.html'


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
        uid = urlsafe_base64_encode(force_bytes(user.pk))  # кодирование id пользователя
        activation_url = reverse_lazy(
            "confirm_email", kwargs={"uidb64": uid, "token": token}
        )
        current_site = Site.objects.get_current().domain
        send_mail(
            message=f"""
            Подтвердите свой адрес электронной почты:
            Пожалуйста, перейдите по ссылке: http://{current_site}{activation_url}
            """,  # сообщение
            from_email=EMAIL_HOST_USER,  # отправитель
            recipient_list=[user.email],  # получатель
            fail_silently=False,  # не пытаемся отправить письмо
        )

        return super().form_valid(form)


User = get_user_model()


class UserConfirmEmailView(LoginRequiredMixin, View):
    """Подтверждение почты пользователя"""
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("users:login")
        else:
            return redirect("email_confirmation_failed")