"""
ダミーサンプルフォーム
"""

from django import forms
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