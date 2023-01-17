from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#model for newsletter users

class NewsLetterUser(models.Model):
    name = models.CharField(max_length=50)
    phone_number= models.CharField(max_length=11)
    email = models.EmailField(unique=True)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    instagram_address = models.URLField(blank=True, max_length=200)
    profile_pic = models.ImageField(blank=True, upload_to='prfile_pics')

    def __str__(self):
        return self.user.username
    
