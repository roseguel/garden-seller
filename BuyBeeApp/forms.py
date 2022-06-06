from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from BuyBeeApp.models import Usuario

# Creo mi propio UserCreationForm, para poder asignar el correo electronico de una vez.
class registrarUsuario(UserCreationForm):
    username = forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField()
    password2=forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# Creo un formulario para poder registrar los datos personales del usuario.
class registroPersonal(ModelForm):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    rut = forms.IntegerField()
    class Meta:
        model = Usuario
        fields = ["rut", "nombreusuario", "nombres", "apellidos", "email"]