#import for signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

#function of receiver after update profile
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,

        )

#function of receiver after delete user
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

#post_save.connect(profileUpdated, sender=Profile)
#post_delete.connect(deleteUser, sender=Profile)