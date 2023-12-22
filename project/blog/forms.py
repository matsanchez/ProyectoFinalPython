from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'body', 'image']
        labels = {
                'title': 'Titulo del Post',
                'subtitle': 'Subtitulo',
                'body': 'Ingrese su experiencia',
                'image': 'Subi una imagen',
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'full-width bg-transparent'})
            field.widget.attrs['placeholder'] = self.Meta.labels.get(field_name, '')
