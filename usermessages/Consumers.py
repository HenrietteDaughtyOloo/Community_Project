import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Community
from .serializers import MessageSerializer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.community_id = self.scope['url_route']['kwargs']['community_id']
        self.room_group_name = f'chat_{self.community_id}'

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
        user = self.scope['user']
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