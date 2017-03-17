from django import forms
from django.contrib.auth.models import User
from imgag.models import UserProfile, Comment, Vote
from registration.forms import RegistrationForm


class UserForm(RegistrationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(RegistrationForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your comment here. (max length: 200)', 'maxlength': 200}))

    class Meta:
        model = Comment
        fields = ('text', )
