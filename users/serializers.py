from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

from users.models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    """Register User Serializer"""
    name = serializers.CharField(
        max_length=120,
        min_length=3,
        required=True,
    )

    @transaction.atomic # Define transaction.atomic to rollback the save operation in case of error
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user

class CustomUserDetailsSerializer(UserDetailsSerializer):
    """User Details Serializer"""

    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'name',
            'username',
        )
        read_only_fields = ('pk', 'email',)