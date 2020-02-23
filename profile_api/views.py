from rest_framework import generics
from profile.models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response

class ListProfilesView(generics.ListAPIView):
    queryset = Profile.objects.exclude(user__is_superuser=True)
    serializer_class = ProfileSerializer