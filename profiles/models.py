from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Profiles Model
    Holds the profile information of users
    Ensures profiles are ordered with creation in descending order
    Returns string containing user's profile picture
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank= True)
    name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    current_employer = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_vpfbb8'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile picture"

def create_profile(sender, instance, created, **kwargs):
    """
    Creates a new profile on new user creation
    Checks if no existing profile associated with the user
    """
    if created and not Profile.objects.filter(owner=instance).exists():
        Profile.objects.create(owner=instance)
        
post_save.connect(create_profile, sender=User)


