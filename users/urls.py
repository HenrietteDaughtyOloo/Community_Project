from django.urls import path
from .views import UserListCreate, UserDetail, RegisterAPI,LoginAPI, UsersByCommunity

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/register/', RegisterAPI.as_view(), name='register'),
    path('users/login/', LoginAPI.as_view(), name='login'),
    path('userscommunity/<int:community_id>/', UsersByCommunity.as_view(), name='users-per-community'),

]