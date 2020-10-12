from django.db import models
# Create your models here.


class ChatApp(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
