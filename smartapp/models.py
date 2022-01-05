from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  profile_pic = CloudinaryField("image")
  bio = models.TextField()
  contact=models.CharField(max_length=100)
  user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
  
def save_profile(self):
    self.save()

def delete_profile(self):
     self.save()

def update_profile(self):
     self.save() 

@classmethod
def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

def _str_(self):
        return self.user.username