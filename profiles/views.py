from rest_framework import generics
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    orders profile list by creation in descending order
    """
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer