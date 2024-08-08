from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password2', 'placeholder':'Confirme contraseña'}))

    class Meta:
        model = User
        fields = ['name', 'last_name', 'birth_date', 'direction', 'cell', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'apellidos', 'placeholder': 'Apellido'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'fechaNaci', 'placeholder': 'Fecha de nacimiento'}),
            'direction': forms.TextInput(attrs={'class': 'direction', 'placeholder': 'Dirección'}),
            'cell': forms.TextInput(attrs={'class': 'cell', 'placeholder': 'Celular'}),
            'email': forms.EmailInput(attrs={'class': 'e-mail', 'placeholder': 'Correo electrónico'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está en uso.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Error las contraseñas no coinciden.")
        return cleaned_data
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'usuario', 'placeholder': 'Correo electrónico'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Contraseña'}))

class FormularioUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'direction', 'cell', 'email']
        labels = {
            'name': 'Nombre',
            'direction': 'Dirección',
            'cell': 'Celular',
            'email': 'Correo electrónico',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nombre'}),
            'direction': forms.TextInput(attrs={'class': 'direction', 'placeholder': 'Dirección'}),
            'cell': forms.TextInput(attrs={'class': 'cell', 'placeholder': 'Celular'}),
            'email': forms.EmailInput(attrs={'class': 'e-mail', 'placeholder': 'Correo electrónico'}),
        }
