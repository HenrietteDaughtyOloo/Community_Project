from venv import logger
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
from rest_framework import generics, status



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

# class JoinCommunity(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     authentication_classes = [JWTAuthentication]

#     def post(self, request, pk, *args, **kwargs):
#         community = Community.objects.get(pk=pk)
#         community.members.add(request.user)
#         return Response({'status': 'joined'}, status=status.HTTP_200_OK)

# class LeaveCommunity(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     authentication_classes = [JWTAuthentication]

#     def post(self, request, pk, *args, **kwargs):
#         community = Community.objects.get(pk=pk)
#         community.members.remove(request.user)
#         return Response({'status': 'left'}, status=status.HTTP_200_OK)
# class DetailsOnCommunity(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Community.objects.all()
#     serializer_class = CommunitySerializer
#     permission_classes = [AllowAny]
#     authentication_classes = [JWTAuthentication]

class JoinCommunity(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk, *args, **kwargs):
        try:
            community = Community.objects.get(pk=pk)
            community.members.add(request.user)
            return Response({'status': 'joined'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error joining community: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LeaveCommunity(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk, *args, **kwargs):
        try:
            community = Community.objects.get(pk=pk)
            community.members.remove(request.user)
            return Response({'status': 'left'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error leaving community: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DetailsOnCommunity(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]