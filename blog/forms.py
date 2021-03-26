from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'slug',
            'tags',
        ]

class PostDeleteForm(ModelForm):
    class Meta:
        model = Post
        fields = []