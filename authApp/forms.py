from django import forms
# from django.contrib.auth import login
from django.contrib.auth.models import User
from django.forms.models import BaseModelFormSet

# from auth.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)


class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class MyFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = User.objects.all().order_by('username')



class UserGroupForm(forms.ModelForm):
    def clean_username(self):
        return self.instance.username