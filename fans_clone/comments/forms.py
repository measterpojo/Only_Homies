from django import forms 

from .models import Comments


class CommentForm(forms.ModelForm):

	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'validate'}), required=True)

	class Meta:
		model = Comments
		fields = ('body',)