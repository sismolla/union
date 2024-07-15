from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class chat_app(models.Model):
    name = models.CharField(max_length=50,null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True,blank=True,default='no content')
    is_admin = models.BooleanField(default=False,null=False)

    def __str__(self):
        return f'message from {self.name} at {self.timestamp}'

