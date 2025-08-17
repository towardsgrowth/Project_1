from django.urls import path
from .views import greeting, contact, channel
urlpatterns = [
    path('greeting/', greeting, name="greeting"),
    path('contact/', contact, name="contact"),
    path('channel/', channel, name="channel")
]