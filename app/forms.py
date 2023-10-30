from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Comments, Subscribe
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content', 'email', 'name', 'course'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Deja tus comentarios, ' \
                                                             'sugerencias o preguntas a continuación. ' \
                                                             'Tu opinión es importante ' \
                                                             'y me ayuda a mejorar  *'
        self.fields['name'].widget.attrs['placeholder'] = "Tu nombre, amigo(a):  *"
        self.fields['email'].widget.attrs['placeholder'] = "Tu correo:  *"



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {'email': _('')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Su correo acá, joven '


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresa un nombre de usuario'
        self.fields['email'].widget.attrs['placeholder'] = "Tu correo acá, amigo(a)"
        self.fields['password1'].widget.attrs['placeholder'] = "Ingresa una contraseña "
        self.fields['password2'].widget.attrs['placeholder'] = "Repite la contraseña  "

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username= username)
        if new.count():
            raise forms.ValidationError("No poh, ese nombre ya está registrado. Intenta otro?")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("El correo ingresado ya se encuentra registrado (me salió verso)")
        return email

    def clean_passwrod2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas deben ser iguales poh!")
        return password2