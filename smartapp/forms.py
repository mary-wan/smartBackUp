from .models import *
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','contact') 