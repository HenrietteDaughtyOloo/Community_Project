from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
from .models import Community
from usermessages.models import Message


class IsAdminOrMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Community):
            return request.user in obj.members.all() or request.user.is_staff
        elif isinstance(obj, Message):
            return request.user in obj.community.members.all() or request.user.is_staff
        return False
class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'member'