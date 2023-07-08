from django import forms
from app.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content', 'email', 'name', 'course'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'cuenta que onda, que opinas de este post *'
        self.fields['name'].widget.attrs['placeholder'] = "Tu nombre, amigo(a) *"
        self.fields['email'].widget.attrs['placeholder'] = "Tu correo: *"
        self.fields['course'].widget.attrs['placeholder'] = "Curso: (si es que quieres) "
