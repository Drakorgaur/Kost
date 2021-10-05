from django import forms

from .models import Note, Test

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('name','main_field','add_field')

class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('field',)

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    class Meta:
        model = User

from .models import RegisterToken


ROLE=[('Admin','Create admin user'),
        ('User','Create default user'),
        ('Mafia','Create Mafia user')]
class RegisterTokenForm(forms.Form):
    role = forms.ChoiceField(choices=ROLE, widget=forms.RadioSelect)
    class Meta:
        model = RegisterToken

class TokenInputForm(forms.Form):
    token = forms.CharField()
    email = forms.EmailField()

class FilterForm(forms.Form):
    filter = forms.CharField()