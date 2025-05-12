from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Identifiant')
    password = forms.CharField(max_length=50, label='Mot de passe', widget=forms.PasswordInput)