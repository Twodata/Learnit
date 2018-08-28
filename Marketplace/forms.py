from django import forms
from .models import market, article, Comment, Internship, UserProfile, Workshop

from django.contrib.auth.models import User



class marketForm(forms.ModelForm):
    class Meta:
        model = market
        exclude = ['added_by']
#        fields = '__all__'
        
        
class articleForm(forms.ModelForm):
    class Meta:
        model = article
        exclude = ['added_by', 'likes', 'views', 'approved_article']

       

class userForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput () )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'image']
        
        
class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        exclude = ['added_by']
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']



class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        exclude = ['added_by']

    
        




