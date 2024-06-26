from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            phone_number='1234567890',
            role=User.MEMBER
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword123'))
        self.assertEqual(self.user.phone_number, '1234567890')
        self.assertEqual(self.user.role, User.MEMBER)
        self.assertEqual(self.user.profile_picture.name, '')  
        self.assertEqual(self.user.about, '') 

    def test_update_user_profile(self):
        self.user.profile_picture = 'profile_pics/test.jpg'
        self.user.about = 'This is a test user.'
        self.user.phone_number = '0987654321'
        self.user.role = User.ADMIN
        self.user.save()

        self.assertEqual(self.user.profile_picture, 'profile_pics/test.jpg')
        self.assertEqual(self.user.about, 'This is a test user.')
        self.assertEqual(self.user.phone_number, '0987654321')
        self.assertEqual(self.user.role, User.ADMIN)

    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            username='superuser',
            password='superpassword123',
            phone_number='1122334455',
            role=User.ADMIN
        )
        self.assertTrue(superuser.is_superuser)
        self.assertEqual(superuser.username, 'superuser')
        self.assertTrue(superuser.check_password('superpassword123'))
        self.assertEqual(superuser.phone_number, '1122334455')
        self.assertEqual(superuser.role, User.ADMIN)

    def test_user_without_phone_number(self):
        user = User.objects.create_user(
            username='usernophone',
            password='password123',
            phone_number=0  
        )
        self.assertEqual(user.phone_number, 0)