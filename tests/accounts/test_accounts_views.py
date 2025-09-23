"""
ダミーサンプルテスト
"""

import pytest
from django.urls import reverse
from accounts.models import CustomUser


@pytest.mark.django_db
def test_dummy_fbv(client) -> None:
    """FBVの動作テスト"""
    url = reverse("accounts:dummy_fbv")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Hello Django from FBV!" in response.content


@pytest.mark.django_db
def test_dummy_cbv(client) -> None:
    """CBVの動作テスト"""
    url = reverse("accounts:dummy_cbv")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Hello Django from CBV!" in response.content


@pytest.mark.django_db
def test_create_user_with_manager() -> None:
    """CustomUserManagerを通じて通常ユーザーを作成できるか"""
    user = CustomUser.objects.create_user(
        email='test@example.com',
        password='password123'
    )
    assert user.email == 'test@example.com'
    assert user.check_password('password123')
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser_with_manager() -> None:
    """CustomUserManagerを通じてスーパーユーザーを作成できるか"""
    admin = CustomUser.objects.create_superuser(
        email='admin@example.com',
        password='adminpass123'
    )
    assert admin.email == 'admin@example.com'
    assert admin.check_password('adminpass123')
    assert admin.is_staff
    assert admin.is_superuser