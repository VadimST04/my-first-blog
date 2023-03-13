from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

        from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-floating'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-floating'}))
