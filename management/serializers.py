from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'fathers_name',
            'mothers_name',
            'team_id',
            'profile_image',
            'address',
            'blood_group',
            'last_seen',
            'email',
        ]