from django import forms
from .models import Blog
 
class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
 
        fields = ['title', 'pub_date', 'body'] 