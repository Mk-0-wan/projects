
# we are going to rearrange how the document should look like
# make an import on the model you want to use for the form creation
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
