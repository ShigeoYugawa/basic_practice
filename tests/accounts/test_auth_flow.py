import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_registration_login_logout_flow(client):
    # --- サインアップ ---
    registration_url = reverse("accounts:registration")  # urls.pyでのname="registration" に合わせる
    registration_data = {
        "email": "testuser@example.com",
        "nickname": "testuser",
        "password1": "strongpassword123",
        "password2": "strongpassword123",
    }
    response = client.post(registration_url, registration_data)
    
    # ユーザーが作成されているか確認
    assert User.objects.filter(email="testuser@example.com").exists()

    # サインアップ直後にリダイレクトが発生する想定
    assert response.status_code == 302  

    # --- ログイン ---
    login_url = reverse("accounts:login")
    login_data = {
        "username": "testuser@example.com",   # 認証方式によっては "email" を使う場合もある
        "password": "strongpassword123",
    }
    response = client.post(login_url, login_data)

    # ログイン成功でリダイレクトが発生
    assert response.status_code == 302

    # リクエストのユーザーが認証済みか確認
    response = client.get(reverse("accounts:welcome_view"))
    assert response.wsgi_request.user.is_authenticated

    # --- ログアウト ---
    logout_url = reverse("accounts:logout")
    response = client.post(logout_url)

    assert response.status_code == 302
    response = client.get(reverse("accounts:welcome_view"))
    assert not response.wsgi_request.user.is_authenticated