# from django.shortcuts import render
# from .serializers import CommunitySerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import *
# from django.http import HttpResponse
# # from rest_framework.permissions import IsAdminOrReadOnly


# # Create your views here.
# @api_view(['GET','PUT','POST','DELETE'])
# def view_communities(request):
#     if request.method == 'GET':
#         communitydata = Community.objects.all()
#         data = {
#             'communitydata':list(communitydata.values())
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     elif request.method =='POST':
#         serializer = CommunitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def view_communities_by_id(request, id):
#         try:
#             community = Community.objects.get(pk=id)
#         except Community.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         if request.method == 'GET':
#             serializer = CommunitySerializer(community)
#             return Response(serializer.data)
#         elif request.method =='PUT':
#             serializer = CommunitySerializer(community, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         elif request == 'DELETE':
#             community.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

# # @api_view(['POST'])
# # @permission_classes([IsAdminOrReadOnly])
# # def create_community(request):
# communities/views.py
# communities/views.py
from rest_framework import generics
from .models import Community
from .serializers import CommunitySerializer
# from .permissions import IsAdminOrReadOnly
from .permissions import IsAdminOrMember
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
