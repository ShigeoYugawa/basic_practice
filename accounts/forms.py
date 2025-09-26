"""
ダミーサンプルフォーム
"""

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
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
    """サインアップ用"""
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "nickname")


class CustomUserChangeForm(UserChangeForm):
    """ユーザー更新用（プロフィール編集など）"""
    class Meta:
        model = CustomUser
        fields = ("email", "nickname")


class CustomLoginForm(AuthenticationForm):
    """ログイン用"""
    username = forms.EmailField(label="Email")  # CustomUser の USERNAME_FIELD が email のため
