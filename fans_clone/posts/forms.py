from django import forms 
from .models import Post

from tier.models import Tier


class NewTierForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}), required=True)
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'validate'}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}), required=True)
	tier = forms.ModelChoiceField(queryset=Tier.objects.all(), required=True)

	class Meta:
		model = Post
		fields = ('content', 'title', 'caption', 'tier')