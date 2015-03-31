from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
