from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Create_Order(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Account_setting(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

