from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
	class Meta:
			model=Profile
			exclude=['username']
        
class BlogPostForm(forms.ModelForm):
	class Meta:
			model=BlogPost
			exclude=['username','neighborhood','profpic']
    
class CommentForm(forms.ModelForm):
	class Meta:
			model = Comment
			exclude=['username','post']
    
class BusinessForm(forms.ModelForm):
	class Meta:
			model = Business
			exclude=['owner','neighborhood']
    
class notificationsForm(forms.ModelForm):
  class Meta:
			model = Update
			exclude=['author','neighborhood','post_date']