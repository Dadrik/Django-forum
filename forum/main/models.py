from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, null=True)
    text = models.TextField()
    parent_id = models.ForeignKey('self', null=True, related_name='childs')


    def __str__(self):
        return self.text
