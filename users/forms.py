# Django imports
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from dj_rest_auth.registration.views import RegisterView

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ('name','email','username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('name','email','username')