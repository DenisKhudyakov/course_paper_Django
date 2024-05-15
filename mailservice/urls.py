from django.urls import path

from mailservice.apps import MailserviceConfig
from mailservice.views import (ClientCreateView, ClientDeleteView,
                               ClientDetailView, ClientListView,
                               ClientUpdateView, HomePageView, LogsListView,
                               MailingSettingsCreateView,
                               MailingSettingsDeleteView,
                               MailingSettingsDetailView,
                               MailingSettingsListView,
                               MailingSettingsUpdateView, MessageCreateView,
                               MessageDeleteView, MessageDetailView,
                               MessageListView, MessageUpdateView)

app_name = MailserviceConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("clients/", ClientListView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
    path("create/", ClientCreateView.as_view(), name="create-client"),
    path("<int:pk>/update/", ClientUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ClientDeleteView.as_view(), name="delete-client"),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
    path("messages/create/", MessageCreateView.as_view(), name="message-create"),
    path(
        "messages/update/<int:pk>/", MessageUpdateView.as_view(), name="message-update"
    ),
    path(
        "messages/delete/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"
    ),
    path("settings/", MailingSettingsListView.as_view(), name="settings"),
    path(
        "settings/<int:pk>/",
        MailingSettingsDetailView.as_view(),
        name="settings-detail",
    ),
    path(
        "settings/create/", MailingSettingsCreateView.as_view(), name="settings-create"
    ),
    path(
        "settings/update/<int:pk>/",
        MailingSettingsUpdateView.as_view(),
        name="setting-update",
    ),
    path(
        "settings/delete/<int:pk>/",
        MailingSettingsDeleteView.as_view(),
        name="setting-delete",
    ),
    path("logs/", LogsListView.as_view(), name="logs"),
]
