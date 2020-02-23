from rest_framework import serializers
from django.contrib.auth.models import User
from profile.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user','birth_date','home_address','home_postal_code','phone_number','lat','lng')