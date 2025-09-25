"""
ダミーサンプルフォーム
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class DummyForm(forms.Form):
    """DBを使わないフォーム"""
    name = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=0, max_value=120)


class DummyUserForm(forms.ModelForm):
    """DBを使うフォーム"""
    class Meta:
        model = CustomUser
        fields = ["email", "password"]


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "nickname")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "nickname")
