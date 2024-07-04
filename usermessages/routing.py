from django.urls import path
from .consumers import ChatConsumer
websocket_urlpatterns = [
    path('ws/chat/<int:community_id>/', ChatConsumer.as_view()),
]