import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Community
from .serializers import MessageSerializer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.community_id = self.scope['url_route']['kwargs']['community_id']
        self.room_group_name = f'chat_{self.community_id}'

        self.user = await sync_to_async(self.get_user_from_token)(self.scope['query_string'])
        if self.user is None or isinstance(self.user, AnonymousUser):
            await self.close()
        else:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.user
        community = await sync_to_async(Community.objects.get)(id=self.community_id)

        message_instance = await sync_to_async(Message.objects.create)(
            community=community, sender=user, content=message)

        serializer = MessageSerializer(message_instance)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': serializer.data
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    def get_user_from_token(self, query_string):
        try:
            token_name, token_key = query_string.decode().split('=')
            if token_name == 'token':
                valid_data = UntypedToken(token_key)
                user = JWTAuthentication().get_user(valid_data)
                return user
        except (InvalidToken, TokenError):
            return AnonymousUser()