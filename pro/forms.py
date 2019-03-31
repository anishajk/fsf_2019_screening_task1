from django import forms
from .models import Comment

class CommentForm(forms.Form):

	username = forms.CharField(max_length=250)
	comment = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ['username','comment'] 