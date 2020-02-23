from django.contrib.auth.admin import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    password = forms.CharField(max_length=255, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password')


class ChangePasswordForm(AdminPasswordChangeForm):
    class Meta:
        model = User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
            label='',
            max_length=255,
            widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter First Name.'}),
    )
    last_name  = forms.CharField(
            label='',
            max_length=255,
            widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter Last Name.'}),
    )
    email = forms.EmailField(
            label='',
            max_length=255,
            widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter E-mail Address'}),
    )

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeate Password'
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['password2'].help_text = "<small>Enter the same password as before, for verification.</small>"
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""



