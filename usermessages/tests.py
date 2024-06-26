from django.test import TestCase
from django.contrib.auth import get_user_model
from communities.models import Community
from usermessages.models import Message

User = get_user_model()

class MessageModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            phone_number='1234567890',
            role=User.MEMBER
        )
        
        self.community = Community.objects.create(
            name='Test Community',
            description='This is a test community.',
            admin=self.user
        )
        
        self.community.members.add(self.user)

    def test_message_creation(self):
        message = Message.objects.create(
            community=self.community,
            sender=self.user,
            content='This is a test message.'
        )
        
        self.assertEqual(message.community, self.community)
        self.assertEqual(message.sender, self.user)
        self.assertEqual(message.content, 'This is a test message.')
        self.assertIsNotNone(message.sent_at)

    def test_str_method(self):
        message = Message.objects.create(
            community=self.community,
            sender=self.user,
            content='This is a test message.'
        )
        
        self.assertEqual(str(message), 'This is a test message')

