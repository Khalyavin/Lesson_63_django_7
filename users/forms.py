from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm

from products.forms_mixins import StyleFormMixin
from users.models import User


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


class CustomUserChangeForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'avatar')


class CustomPasswordChangeForm(StyleFormMixin, PasswordChangeForm):

    class Meta:
        model = User
        fields = '__all__'


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserPasswordResetEmailForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('email',)
