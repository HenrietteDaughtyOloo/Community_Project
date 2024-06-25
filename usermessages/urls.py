from django.urls import path
from .views import CreateListOfMessages, MessageDetails

urlpatterns = [
    path('messages/', CreateListOfMessages.as_view(), name='created_list_of_messages'),
    path('messages/<int:pk>/', MessageDetails.as_view(), name='message-details'),
]
