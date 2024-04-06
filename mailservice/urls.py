from mailservice.apps import MailserviceConfig
from django.urls import path
from mailservice.views import HomePageView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView

app_name = MailserviceConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('create/', ClientCreateView.as_view(), name='create-client'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='delete-client')
]

