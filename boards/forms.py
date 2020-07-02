from django import forms
from .models import Topic
from .models import Post
class NewTopicForm(forms.ModelForm):
	message=forms.CharField(widget=forms.Textarea(
		attrs={'rows':5,'placeholder':'Hey,Add something ;-)'}
		),max_length=4000,help_text='Maximum length is 4000')
	class Meta:
		model=Topic
		fields=['subject','message']

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['message', ]