from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Comment
from django import forms


# class SomeForm(forms.Form):
# 	foo = forms.CharField(widget=SummernoteWidget())

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')