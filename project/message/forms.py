from django import forms
from .models import Comments

class MessagePostForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['body']

        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }