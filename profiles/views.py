from rest_framework import generics


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    orders profile list by creation in descending order
    """
    queryset = Profile.objects.all().order_by('-created_at')
    