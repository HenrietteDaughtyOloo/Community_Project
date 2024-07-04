from django.http import HttpResponse
from requests import Response
# ####
from .models import *
from django.http import JsonResponse
from .serializers import *
from .serializers import MessageSerializer
from rest_framework import generics
from .models import Message
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from communities.permissions import IsAdminOrMember, IsMember
from django.conf import settings
from Crypto.Cipher import AES
import base64
import hashlib


secret_key = settings.SECRET_KEY
key = hashlib.sha256(secret_key.encode()).digest()

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(nonce + tag + ciphertext).decode()

def decrypt_message(encrypted_message):
    data = base64.b64decode(encrypted_message.encode())
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    message = cipher.decrypt_and_verify(ciphertext, tag)
    return message.decode()


class CreateListOfMessages(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated,IsMember]


    def perform_create(self, serializer):
        content = serializer.validated_data.get('content')
        encrypted_content = encrypt_message(content)
        serializer.save(sender=self.request.user, content=encrypted_content)

    def get_queryset(self):
        community_id = self.request.query_params.get('community_id')
        return Message.objects.filter(community_id=community_id)

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsAdminOrMember]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.content = decrypt_message(instance.content)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_view(request):
    return Response({'message': 'This is a secure endpoint'})
