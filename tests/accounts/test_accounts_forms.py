"""
ダミーサンプルテスト
"""

import pytest
from accounts.forms import DummyForm, DummyUserForm
from accounts.models import CustomUser


# --- DBを使わないフォームのテスト ---
def test_dummy_form_valid():
    """正しい入力でフォームが有効になる"""
    form_data = {"name": "Alice", "age": 30}
    form = DummyForm(data=form_data)
    assert form.is_valid() is True


def test_dummy_form_invalid():
    """不正な入力でフォームが無効になる"""
    form_data = {"name": "", "age": -5}  # name 空, age がマイナス
    form = DummyForm(data=form_data)
    assert form.is_valid() is False
    assert "name" in form.errors
    assert "age" in form.errors


# --- DBを使うフォームのテスト ---
@pytest.mark.django_db
def test_dummy_user_form_valid():
    form_data = {"email": "test@example.com", "password": "password123"}
    form = DummyUserForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_dummy_user_form_invalid():
    form_data = {"email": "invalid-email", "password": ""}
    form = DummyUserForm(data=form_data)
    assert not form.is_valid()
