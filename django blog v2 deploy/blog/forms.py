from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=True, label="Title")
    content = forms.CharField(required=True, label="Content")
    image = forms.ImageField(required=False, label="Image")
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
