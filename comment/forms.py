from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Comment
        fields = ('content',)
