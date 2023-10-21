from django import forms
from .models import Post, Comment, TagPost
from django.utils.text import slugify


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('choice', 'title', 'text', 'img', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class TagForm(forms.ModelForm):
    class Meta:
        model = TagPost
        fields = ['tag']

    def clean(self):
        cleaned_data = super().clean()
        tag = cleaned_data.get('tag')
        if tag:
            cleaned_data['slug'] = slugify(tag)

        return cleaned_data