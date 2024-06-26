from rest_framework import generics
from .models import Community
from .serializers import CommunitySerializer
# from .permissions import IsAdminOrReadOnly
from .permissions import IsMember
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny


class CreateCommunityList(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]



    def perform_create(self, serializer):
        community = serializer.save()
        community.members.add(self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def join(self, request, pk=None):
        community = self.get_object()
        community.members.add(request.user)
        return Response({'status': 'joined'})
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def leave(self, request, pk=None):
        community = self.get_object()
        community.members.remove(request.user)
        return Response({'status': 'left'})



class DetailsOnCommunity(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
