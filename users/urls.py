from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateView, UserLogin, UserUpdateView,
                         VerificationFailedView, activate)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  # logout
    path("register/", UserCreateView.as_view(), name="register"),  # register
    path("activate/<str:uidb64>/<str:token>/", activate, name="activate"),  # activate
    path(
        "verivication_failed/",
        VerificationFailedView.as_view(),
        name="email_confirmation_failed",
    ),
    path("profile/", UserUpdateView.as_view(), name="profile"),
]
