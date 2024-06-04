from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from . models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField (label ='Usuario',widget=forms.TextInput(attrs= {'autofocus':'True','class':'form-control'}))
    password = forms.CharField (label='Contraseña',widget= forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs= {'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(label='Correo Electronico',widget=forms.EmailInput(attrs= {'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class MyPasswordResetForm(PasswordChangeForm):
    pass

#clase para los datos del usuario
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nombre','fecha','bitacora']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'bitacora': forms.TextInput(attrs={'class': 'form-control'}),
        }


