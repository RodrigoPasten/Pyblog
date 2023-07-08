from django import forms
from app.models import Comments


class CommentForm(forms.ModelForm):
    course = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Curso (opcional)'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu nombre:'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email:'}))
    class Meta:
        model = Comments
        fields = {'content', 'email', 'name', 'course'}
