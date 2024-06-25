from django.db import models
from users.models import User

class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='communityicons/', blank=True)
    description = models.TextField(blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="administered_communities")
    members = models.ManyToManyField(User, related_name='communities')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def joinedStatus(self):
        return self.members.filter(id=User.id).exists()
    
    def join_community(self, user):
        if user not in self.members.all():
            self.members.add(user)
    
    def leave_community(self, user):
        if user in self.members.all():
            self.members.remove(user)

