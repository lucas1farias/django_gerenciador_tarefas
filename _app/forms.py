

from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    username = forms.CharField(label='Nome de usuário', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Senha', max_length=100)
    password_repeat = forms.CharField(label='Repetir senha', max_length=100)
