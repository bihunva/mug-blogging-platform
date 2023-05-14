from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_summernote.fields import SummernoteTextField, SummernoteTextFormField
from django_summernote.widgets import SummernoteInplaceWidget

from blog.models import User, Comment, Post


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..", "class": "search-input"})
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "username"})
    )
    first_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "first name"})
    )
    last_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "last name"})
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "email"})
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "password"})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "password again"})
    )

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
    body = SummernoteTextField()

    class Meta:
        model = Post
        fields = ["title", "body"]
