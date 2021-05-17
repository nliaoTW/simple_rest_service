from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profile_api import serializers
from profile_api import models
from profile_api import permissions


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.SimpleServiceSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
