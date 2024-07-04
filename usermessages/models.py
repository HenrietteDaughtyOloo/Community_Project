from django.db import models
from users.models import User
from communities.models import Community

class Message(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} - {self.content[:20]}"