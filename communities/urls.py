from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CreateCommunityList, DetailsOnCommunity, JoinCommunity, LeaveCommunity



urlpatterns = [
    path('communities/', CreateCommunityList.as_view(), name='community-list'),
    path('communities/<int:pk>/', DetailsOnCommunity.as_view(), name='community-details'),
    path('communities/<int:pk>/join/', JoinCommunity.as_view(), name='community-join'),
    path('communities/<int:pk>/leave/', LeaveCommunity.as_view(), name='community-leave'),
]
