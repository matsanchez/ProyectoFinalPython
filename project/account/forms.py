from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    pass



class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
                'username': 'Nombre de Usuario',
                'email': 'Correo Electrónico',
                'password1': 'Contraseña',
                'password2': 'Confirmar Contraseña',
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'full-width bg-transparent'})
            field.widget.attrs['placeholder'] = self.Meta.labels.get(field_name, '')
    
    def clean_email(self):
        email_field = self.cleaned_data['email']

        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Este correo electronico ya esta registrado')
        
        return email_field
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password1', forms.ValidationError('Las contraseñas no coinciden'))
            self.add_error('password2', forms.ValidationError('Las contraseñas no coinciden'))
 
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','description', 'avatar', 'email', 'link_url','birthday']


