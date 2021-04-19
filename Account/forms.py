from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms.widgets import NumberInput
from django_countries.widgets import CountrySelectWidget

from Account.models import UserProfile
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneNumber = forms.CharField(validators=[phone_regex], max_length=17, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '+237 678248748'}))
    dob = forms.DateField(widget=NumberInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta():
        model = UserProfile
        fields = ('dob', 'phoneNumber', 'country', 'profileImage')
        widgets = {'country': CountrySelectWidget()}
