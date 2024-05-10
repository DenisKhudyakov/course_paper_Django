from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, UserLogin, UserConfirmEmailView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # logout
    path("register/", UserCreateView.as_view(), name="register"),  # register
    path("activate/<uidb64>/<token>/", UserConfirmEmailView.as_view(), name="activate"),  # activate
]
