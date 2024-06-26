from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Community

User = get_user_model()

class CommunityModelTests(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpassword', phone_number='1234567890')
        self.user2 = User.objects.create_user(username='user2', password='testpassword', phone_number='0987654321')
        self.admin_user = User.objects.create_user(username='admin', password='testpassword', phone_number='1122334455')
        
        self.community = Community.objects.create(
            name='Test Community',
            description='This is a test community',
            admin=self.admin_user
        )
    
    def test_community_creation(self):
        self.assertEqual(self.community.name, 'Test Community')
        self.assertEqual(self.community.description, 'This is a test community')
        self.assertEqual(self.community.admin, self.admin_user)
        self.assertEqual(self.community.members.count(), 0)

    def test_join_community(self):
        self.community.join_community(self.user1)
        self.assertIn(self.user1, self.community.members.all())
        self.assertEqual(self.community.members.count(), 1)

    def test_leave_community(self):
        self.community.join_community(self.user1)
        self.community.leave_community(self.user1)
        self.assertNotIn(self.user1, self.community.members.all())
        self.assertEqual(self.community.members.count(), 0)
        
    def test_joined_status_property(self):
        self.community.join_community(self.user1)
        self.community.join_community(self.user2)
        self.assertTrue(self.community.members.filter(id=self.user1.id).exists())
        self.assertTrue(self.community.members.filter(id=self.user2.id).exists())
        self.assertFalse(self.community.members.filter(id=self.admin_user.id).exists())
