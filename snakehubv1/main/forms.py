from django import forms
from main.models import NewsLetterUser
from django.contrib.auth.models import User
from main.models import UserProfileInfo



class NewsLetterUserForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetterUser
        fields = "__all__"


class UserForm(forms.ModelForm):
    password= forms.CharField(widget =forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields= ('instagram_address','profile_pic')