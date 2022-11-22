from django.db import models
from django.contrib.auth.models import User
import uuid

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "OTHER"),
)


class Profile(models.Model):
    """model for user account"""
    image = models.ImageField(upload_to='profileimages/', default='profileimages/profile-avatar.png', null=False,
                              blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    username = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.username
