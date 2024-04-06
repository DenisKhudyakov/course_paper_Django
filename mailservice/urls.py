from mailservice.apps import MailserviceConfig
from django.urls import path
from mailservice.views import HomePageView, ClientListView

app_name = MailserviceConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('clients/', ClientListView.as_view(), name='clients'),
]

