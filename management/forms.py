from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fathers_name', 'mothers_name', 'team_id', 'profile_image', 'address', 'blood_group', 'email']
