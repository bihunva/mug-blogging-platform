from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

from blog.models import User, Comment, Post


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title.."})
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
