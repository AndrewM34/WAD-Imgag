from django import forms
from django.contrib.auth.models import User
from imgag.models import UserProfile, Comment, Vote


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your comment here.', 'maxlength': 200}))

    class Meta:
        model = Comment
        fields = ('text', )
