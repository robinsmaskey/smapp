from django.db import models
import uuid
from useraccounts.models import Profile


class Post(models.Model):
    """Post Model"""
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False, related_name='posts')
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, related_name='postlikes')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment Model"""
    content = models.CharField(max_length=200, null=False, blank=False)
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT, null=False, blank=False, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.post) + " " + str(self.owner)



