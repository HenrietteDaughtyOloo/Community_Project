from rest_framework import serializers
from users.serializers import UserSerializer
from .permissions import IsAdminOrMember
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Community
        fields = '__all__'
        permission_classes = [IsAdminOrMember]