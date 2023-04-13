from django.forms import ModelForm
from django import forms
from .models import BlogWrite


class BlogWriteForm(ModelForm):

    class Meta:
        model = BlogWrite
        fields = ("title", "description", 'blog_img')
