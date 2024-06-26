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
from rest_framework import viewsets


class CreateCommunityList(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]


    def list(self, request):
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        community = serializer.save()
        community.members.add(self.request.user)

    def post(self, request, *args, **kwargs):
        if 'join' in request.data:
            return self.join(request, *args, **kwargs)
        elif 'leave' in request.data:
            return self.leave(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def join(self, request, *args, **kwargs):
        community = self.get_object()
        community.members.add(request.user)
        return Response({'status': 'joined'})

    def leave(self, request, *args, **kwargs):
        community = self.get_object()
        community.members.remove(request.user)
        return Response({'status': 'left'})



class DetailsOnCommunity(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
