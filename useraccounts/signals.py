from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User


def create_profile(sender, instance, created, **kwargs):
    """On create of user record creates profile record"""
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


def update_user(sender, instance, created, **kwargs):
    """On change of profile record update user with same details"""
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    """"On delete of profile record delete related user record"""
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
