from django.urls import path
from .views import CreateCommunityList, DetailsOnCommunity


urlpatterns = [
    path('communities/', CreateCommunityList.as_view(), name='community-list'),
    path('communities/<int:pk>/', DetailsOnCommunity.as_view(), name='community-details'),
]