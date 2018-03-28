from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
  content = models.CharField(max_length=500)
  sender_user = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
  recipient_user = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.sender_user.username