from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import User
from rest_framework import permissions

class UserSerializer(serializers.ModelSerializer):
    # groups = serializers.PrimaryKeyRelatedField(many =True, queryset=Group.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role','profile_picture','phone_number','about']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        user = User.objects.create(
           username = validated_data['username'],
           email = validated_data['email'],
           password = validated_data['password'],
           phone_number = validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user