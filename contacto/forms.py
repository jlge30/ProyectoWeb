from django import forms
from django.core.validators import EmailValidator

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Correo Electrónico",
        max_length=254,
        validators=[EmailValidator(message="Introduce una dirección de correo electrónico válida.")])
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)


