from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields=('comment_name','comment_text')
        exclude = ('file_detail',)